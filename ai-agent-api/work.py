from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from tool_mapping import TOOL_MAPPING
from collection.ConfigArchive import config_archive_tools
from collection.ConnectionMetadata import connection_meta_tools
from flask_cors import CORS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chains.conversation.memory import ConversationSummaryMemory
import json

app = Flask(__name__)
CORS(app)

# Bind tools to the model
all_tools = []
all_tools.extend(config_archive_tools)
all_tools.extend(connection_meta_tools)

# Initialize model with tools
llm = ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000)
all_tools = config_archive_tools + connection_meta_tools
llm_with_tools = llm.bind_tools(all_tools)

# Initialize conversation memory with updated method
memory = ConversationSummaryMemory(llm=llm)
query = ""

@app.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    global query
    """Processes a query through GPT-4 and returns the function name and metadata."""

    print("/ask-gpt called")
    # try:
    data = request.json
    query = data.get("query", "")
    # Load conversation history
    history = memory.load_memory_variables({})['history']
    messages = []        
    if history:
        messages.append(SystemMessage(content=f"Conversation context: {history}"))
    messages.append(HumanMessage(content=query))
    # Get model response
    response = llm_with_tools.invoke(messages)
    print("query : ",query)
    if not query:
        return jsonify({"success": False, "error": "Query is required"}), 400
    # Invoke the model with the query
    # Process tool calls
    tool_responses = []
    tool_calls = response.additional_kwargs.get("tool_calls", [])
    if not tool_calls:
        tool_responses.append(f"not tool found for a {query}")
        final_response = "\n".join(tool_responses) if tool_responses else response.content
        memory.save_context({"input": query}, {"output": final_response})
        print("final_response : ",final_response)
        return jsonify({"success": False, "error": final_response}), 500

    call = tool_calls[0]['function']['name']
    if call in TOOL_MAPPING:
        _, meta_data = TOOL_MAPPING[call]
        tool_responses.append(f"{call} function name received as result")
        final_response = "\n".join(tool_responses) if tool_responses else response.content
        # Update memory
        memory.save_context({"input": query}, {"output": final_response})
        return jsonify({"tool_name": call, "meta_data": meta_data, "success": True})            
    # except Exception as e:
    #     print("errorr : ",e)
    #     return jsonify({"success": False, "error": str(e)}), 500


@app.route('/execute_tool', methods=['POST'])
def execute_tool():
    """Executes a tool based on the provided tool name and arguments."""
    global query
    try:
        data = request.get_json()
        tool_name = data.get("tool_name")
        tool_arguments = data.get("arguments", {})
        print("query : ",query)

        # Load conversation history
        history = memory.load_memory_variables({})['history']
        messages = []        
        if history:
            messages.append(SystemMessage(content=f"Conversation context: {history}"))
        messages.append(HumanMessage(content=query))
        response = llm_with_tools.invoke(messages)


        if not tool_name:
            memory.save_context({"input": query}, {"output": "NO Tool is found"})
            return jsonify({"success": False, "error": "Tool name is required"}), 400

        tool_responses = []
        if tool_name in TOOL_MAPPING:
            function_, _ = TOOL_MAPPING[tool_name]
            try:                
                result = function_.invoke(input={})
                if 'error' in result:                    
                    tool_responses.append(f"{tool_name} executed. Result: {result['error']}")
                    final_response = "\n".join(tool_responses) if tool_responses else response.content
                    return jsonify({"result": final_response, "success": False})
                
                tool_responses.append(f"{tool_name} executed. Result: {result}")
                final_response = "\n".join(tool_responses) if tool_responses else response.content
                return jsonify({"result": final_response, "success": True})
            except Exception as e:
                tool_responses.append(f"{tool_name} executed. Result: {str(e)}")
                final_response = "\n".join(tool_responses) if tool_responses else response.content
                memory.save_context({"input": query}, {"output": final_response})
                return jsonify({"result": final_response, "success": False})

        tool_responses.append(f"{tool_name} executed. Result: No matching tool found")
        final_response = "\n".join(tool_responses) if tool_responses else response.content
        memory.save_context({"input": query}, {"output": final_response})
        return jsonify({"result": final_response, "success": False}),400

    except Exception as e:
        tool_responses.append(f"{tool_name} executed. Result: {str(e)}")
        final_response = "\n".join(tool_responses) if tool_responses else response.content
        memory.save_context({"input": query}, {"output": final_response})
        return jsonify({"result": final_response, "success": False}),500


if __name__ == '__main__':
    app.run(debug=True)
