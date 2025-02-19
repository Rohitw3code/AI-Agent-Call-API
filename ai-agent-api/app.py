from flask import Flask, request, jsonify, make_response
from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationSummaryMemory
from tool_mapping import TOOL_MAPPING
from collection.ConfigArchive import config_archive_tools
from collection.ConnectionMetadata import connection_meta_tools
from langchain_core.messages import HumanMessage, SystemMessage
from flask_cors import CORS
import json
import uuid

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Initialize model with tools
llm = ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000)
all_tools = config_archive_tools + connection_meta_tools
llm_with_tools = llm.bind_tools(all_tools)

# Dictionary to store conversation memories
session_memories = {}

def get_session_id(request):
    """Get or create session ID from cookies"""
    session_id = request.cookies.get('session_id')
    if not session_id or session_id not in session_memories:
        session_id = str(uuid.uuid4())
        session_memories[session_id] = {
            'memory': ConversationSummaryMemory(llm=llm),
            'pending_tools': []
        }
    return session_id

@app.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    """Processes a query through GPT-4 with conversation memory"""
    try:
        data = request.json
        query = data.get("query", "")
        
        # Get or create session ID
        session_id = get_session_id(request)
        
        print(f"Processing query for session {session_id}: {query}")
        
        # Get session memory
        memory_obj = session_memories[session_id]
        memory = memory_obj['memory']
        
        # Prepare messages with conversation history
        history = memory.load_memory_variables({}).get('history', '')
        messages = []
        if history:
            messages.append(SystemMessage(content=f"Conversation context: {history}"))
        messages.append(HumanMessage(content=query))
        
        # Get model response
        response = llm_with_tools.invoke(messages)
        
        # Process tool calls
        tool_responses = []
        tool_calls = response.additional_kwargs.get("tool_calls", [])
        memory_obj['pending_tools'] = []  # Reset pending tools
        
        for call in tool_calls:
            func_name = call['function']['name']
            args = json.loads(call['function']['arguments'])
            
            if func_name in TOOL_MAPPING:
                tool_responses.append(f"Tool {func_name} identified")
                memory_obj['pending_tools'].append({
                    'name': func_name,
                    'args': args
                })
            else:
                tool_responses.append(f"Tool {func_name} not found")
        
        final_response = "\n".join(tool_responses) if tool_responses else response.content
        
        # Save to memory regardless of tool presence
        memory.save_context({"input": query}, {"output": final_response})

        # Prepare response
        response = None
        if memory_obj['pending_tools']:
            tool_info = memory_obj['pending_tools'][0]  # Return first tool
            _, meta_data = TOOL_MAPPING[tool_info['name']]
            response = jsonify({
                "tool_name": tool_info['name'],
                "meta_data": meta_data,
                "success": True
            })
        else:
            response = jsonify({
                "result": final_response,
                "success": True
            })
        
        # Set session cookie if new session was created
        if not request.cookies.get('session_id'):
            response.set_cookie('session_id', session_id, httponly=True, samesite='Lax')
        
        return response

    except Exception as e:
        print(f"Error in ask_gpt: {str(e)}")
        return jsonify({"error": str(e), "success": False}), 500

@app.route('/execute_tool', methods=['POST'])
def execute_tool():
    """Executes a tool based on the provided tool name and arguments."""
    # try:
    data = request.get_json()
    func_name = data.get("tool_name")
    print("funcname ",func_name)
    
    # Get session ID from cookies
    session_id = get_session_id(request)
    memory_obj = session_memories.get(session_id)
    
    if not memory_obj:
        print("memory obj ---")
        return jsonify({"success": False, "error": "Invalid session"}), 400
        
    pending_tools = memory_obj['pending_tools']
    
    # Find the matching tool in pending tools
    tool_data = next((t for t in pending_tools if t['name'] == func_name), None)
    
    print("tool : ",tool_data)
    if not tool_data:
        return jsonify({"success": False, "result": "Tool not found in session"}), 400
        
    # try:
    # Execute the tool
    tool_func, data_processor = TOOL_MAPPING[func_name]
    processed_args = data_processor(tool_data['args'])
    result = tool_func(processed_args)
    
    # Save execution result to memory
    execution_response = f"{func_name} executed successfully. Result: {result}"
    memory_obj['memory'].save_context(
        {"input": f"Execute {func_name}"},
        {"output": execution_response}
    )
    
    print("result : ",result)
    return jsonify({"result": result, "success": True})
        
    # except Exception as e:
    #     error_msg = f"Error executing {func_name}: {str(e)}"
    #     memory_obj['memory'].save_context(
    #         {"input": f"Execute {func_name}"},
    #         {"output": error_msg}
    #     )
    #     return jsonify({"result": error_msg, "success": False})

    # except Exception as e:
    #     return jsonify({"success": False, "result": "3 : "+str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)