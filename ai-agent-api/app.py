from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chains.conversation.memory import ConversationSummaryMemory
from tool_mapping import TOOL_MAPPING
from collection.ConfigArchive import config_archive_tools
from collection.ConnectionMetadata import connection_meta_tools
import json

app = Flask(__name__)
CORS(app)

# Initialize model and tools
llm = ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000)
all_tools = config_archive_tools + connection_meta_tools
llm_with_tools = llm.bind_tools(all_tools)

# Initialize conversation memory
memory = ConversationSummaryMemory(llm=llm)

def get_conversation_context():
    """Retrieve and format conversation history."""
    history = memory.load_memory_variables({}).get('history', '')
    messages = [SystemMessage(content=f"Conversation context: {history}")] if history else []
    return messages

@app.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    """Processes a query through GPT-4 and returns a response."""
    data = request.json
    query = data.get("query", "").strip()
    
    if not query:
        return jsonify({"type": "error", "error": "Query is required"}), 400

    print("/ask_gpt called with query:", query)
    
    messages = get_conversation_context() + [HumanMessage(content=query)]
    response = llm_with_tools.invoke(messages)
    
    tool_calls = response.additional_kwargs.get("tool_calls", [])
    print("tool_calls:", tool_calls)
    
    if not tool_calls:
        # Generate response based on memory and query if no tool is found
        final_response = response.content
        print("Generated response:", final_response)
        return jsonify({"type":"ai-response","ai": final_response})
    
    tool_name = tool_calls[0]['function']['name']
    if tool_name in TOOL_MAPPING:
        _, meta_data = TOOL_MAPPING[tool_name]
        success_message = f"{tool_name} function name received as result"
        print("Success message:", success_message)
        return jsonify({"tool_name": tool_name, "meta_data": meta_data, "type":"tool"})
    
    return jsonify({"type": "error", "error": "Tool not found in mapping"}), 500

@app.route('/execute_tool', methods=['POST'])
def execute_tool():
    """Executes a tool based on the provided tool name and arguments."""
    data = request.get_json()
    tool_name = data.get("tool_name", "").strip()
    tool_arguments = data.get("arguments", {})
    
    if not tool_name:
        return jsonify({"type": "error", "error": "Tool name is required"}), 400
    
    print("/execute_tool called for:", tool_name)
    messages = get_conversation_context() + [HumanMessage(content=tool_name)]
    response = llm_with_tools.invoke(messages)
    
    tool_responses = []
    
    
    if tool_name in TOOL_MAPPING:
        function_, _ = TOOL_MAPPING[tool_name]
        try:
            print("Invoking tool with arguments:", tool_arguments)
            result = function_.invoke(input=tool_arguments)
            print("Tool execution result:", result)
            tool_responses.append(f"{tool_name} executed. Result: {result}")
        except Exception as e:
            error_message = f"Error executing {tool_name}: {str(e)}"
            print(error_message)
            tool_responses.append(error_message)
    else:
        error_message = "No matching tool found"
        print(error_message)
        tool_responses.append(error_message)
    
    final_response = "\n".join(tool_responses)
    memory.save_context({"input": tool_name}, {"output": final_response})
    
    return jsonify({"type":"result","result": final_response, "success": True if tool_responses else False})

if __name__ == '__main__':
    app.run(debug=True)
