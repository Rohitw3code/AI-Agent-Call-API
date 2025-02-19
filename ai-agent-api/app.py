from flask import Flask, request, jsonify
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
CORS(app)

# Initialize model with tools
llm = ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000)
all_tools = config_archive_tools + connection_meta_tools
llm_with_tools = llm.bind_tools(all_tools)

# Dictionary to store conversation memories
session_memories = {}
response = llm_with_tools.invoke("Welcome to PingFederate Admin API Assistant! How can I help you today?")
# Initialize conversation memory with updated method
memory = ConversationSummaryMemory(llm=llm)
query = ""
messages = []

@app.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    """Processes a query through GPT-4 with conversation memory"""
    try:
        data = request.json
        query = data.get("query", "")
        session_id = data.get("session_id", str(uuid.uuid4()))
        
        print(f"Processing query for session {session_id}: {query}")
                
        # Load conversation history
        history = memory.load_memory_variables({})['history']
        
        if history:
            messages.append(SystemMessage(content=f"Conversation context: {history}"))
        messages.append(HumanMessage(content=query))
        
        # Get model response
        response = llm_with_tools.invoke(messages)
        
        # Process tool calls
        tool_responses = []
        tool_calls = response.additional_kwargs.get("tool_calls", [])
        print("Detected tool calls:", tool_calls)
        
        for call in tool_calls:
            func_name = call['function']['name']
            args = json.loads(call['function']['arguments'])
            
            if func_name in TOOL_MAPPING:
                try:
                    tool_func = TOOL_MAPPING[func_name][0]
                    result = tool_func.invoke(input=args)
                    tool_responses.append(f"{func_name} executed. Result: {result}")
                except Exception as e:
                    tool_responses.append(f"Error executing {func_name}: {str(e)}")
            else:
                tool_responses.append(f"Tool {func_name} not found")
        
        final_response = "\n".join(tool_responses) if tool_responses else response.content
        
        # Update memory
        memory.save_context({"input": query}, {"output": final_response})

        if func_name in TOOL_MAPPING:
            _, meta_data = TOOL_MAPPING[func_name]
            return jsonify({"tool_name": func_name, "meta_data": meta_data, "success": True})

        return jsonify({"success": False, "error": "No matching tool found"}), 400
        
    except Exception as e:
        print("error in ask_gpt")
        return jsonify({"error": "3"+str(e), "success": False}), 500

tool_responses = []

@app.route('/execute_tool', methods=['POST'])
def execute_tool():
    """Executes a tool based on the provided tool name and arguments."""
    try:
        data = request.get_json()
        func_name = data.get("tool_name")
        tool_arguments = data.get("arguments", {})

        if not func_name:
            return jsonify({"success": False, "error": "Tool name is required"}), 400

        if func_name in TOOL_MAPPING:
            function_, _ = TOOL_MAPPING[func_name]
            try:
                result = function_(tool_arguments.get("param", {}), tool_arguments.get("data", {}))
                if 'error' in result:
                    return jsonify({"result": result['error'], "success": False})
                return jsonify({"result": result, "success": True})
            except Exception as e:
                return jsonify({"result": str(e), "success": False})
        
        # return jsonify({"success": False, "result": "No matching tool found"}), 400

        if func_name in TOOL_MAPPING:
            try:
                tool_func = TOOL_MAPPING[func_name][0]
                # Proper invocation with arguments
                result = tool_func.invoke(input=tool_arguments)
                print("result : ", result)
                tool_responses.append(f"{func_name} executed. Result: {result}")
            except Exception as e:
                tool_responses.append(f"Error executing {func_name}: {str(e)}")
        else:
            tool_responses.append(f"Tool {func_name} not found")
    
        final_response = "\n".join(tool_responses) if tool_responses else response.content
        # Update memory
        memory.save_context({"input": query}, {"output": final_response})
        return jsonify({"result": final_response, "success": True})
    except Exception as e:
        return jsonify({"success": False, "result": str(e)}), 500







if __name__ == '__main__':
    app.run(debug=True)