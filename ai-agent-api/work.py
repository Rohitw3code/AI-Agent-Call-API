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
all_tools = config_archive_tools + connection_meta_tools
llm = ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000)
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
    """Processes a query through GPT-4 and returns the function name and metadata."""
    data = request.json
    query = data.get("query", "").strip()
    
    if not query:
        return jsonify({"success": False, "error": "Query is required"}), 400

    print("/ask-gpt called with query:", query)
    
    messages = get_conversation_context() + [HumanMessage(content=query)]
    response = llm_with_tools.invoke(messages)
    
    tool_calls = response.additional_kwargs.get("tool_calls", [])
    if not tool_calls:
        error_message = f"No tool found for query: {query}"
        memory.save_context({"input": query}, {"output": error_message})
        return jsonify({"success": False, "error": error_message}), 500

    tool_name = tool_calls[0]['function']['name']
    if tool_name in TOOL_MAPPING:
        _, meta_data = TOOL_MAPPING[tool_name]
        success_message = f"{tool_name} function name received as result"
        memory.save_context({"input": query}, {"output": success_message})
        return jsonify({"tool_name": tool_name, "meta_data": meta_data, "success": True})
    
    return jsonify({"success": False, "error": "Tool not found in mapping"}), 500

@app.route('/execute_tool', methods=['POST'])
def execute_tool():
    """Executes a tool based on the provided tool name and arguments."""
    data = request.get_json()
    tool_name = data.get("tool_name", "").strip()
    tool_arguments = data.get("arguments", {})
    
    if not tool_name:
        return jsonify({"success": False, "error": "Tool name is required"}), 400
    
    print("/execute_tool called for:", tool_name)
    messages = get_conversation_context() + [HumanMessage(content=tool_name)]
    response = llm_with_tools.invoke(messages)
    
    if tool_name in TOOL_MAPPING:
        function_, _ = TOOL_MAPPING[tool_name]
        try:
            result = function_.invoke(input=tool_arguments)
            output_message = result.get("error", result)
            memory.save_context({"input": tool_name}, {"output": output_message})
            return jsonify({"result": f"{tool_name} executed. Result: {output_message}", "success": True})
        except Exception as e:
            error_message = str(e)
    else:
        error_message = "No matching tool found"
    
    memory.save_context({"input": tool_name}, {"output": error_message})
    return jsonify({"result": f"{tool_name} executed. Result: {error_message}", "success": False}), 500

if __name__ == '__main__':
    app.run(debug=True)
