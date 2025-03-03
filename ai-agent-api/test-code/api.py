from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from tool_mapping import TOOL_MAPPING
from collection.ConfigArchive import config_archive_tools
from collection.ConnectionMetadata import connection_meta_tools
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Initialize the OpenAI GPT-4 model
model = ChatOpenAI(model="gpt-4")

# Bind tools to the model
all_tools = []
all_tools.extend(config_archive_tools)
all_tools.extend(connection_meta_tools)

model = model.bind_tools(all_tools)

@app.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    """Processes a query through GPT-4 and returns the function name and metadata."""

    print("/ask-gpt called")
    try:
        data = request.json
        query = data.get("query", "")

        print("query : ",query)

        if not query:
            return jsonify({"success": False, "error": "Query is required"}), 400

        # Invoke the model with the query
        response = model.invoke(query)
        tool_calls = response.additional_kwargs.get("tool_calls", [])
        print("tool calls : ",tool_calls)

        if tool_calls == []:
            return jsonify({"success": False, "error": "improve your query no tool found"}), 400

        tool_name = tool_calls[0]['function']['name']

        # Retrieve metadata only (no function execution)
        if tool_name in TOOL_MAPPING:
            _, meta_data = TOOL_MAPPING[tool_name]
            return jsonify({"tool_name": tool_name, "meta_data": meta_data, "success": True})

        return jsonify({"success": False, "error": "No matching tool found"}), 400

    except Exception as e:
        print("errorr : ",e)
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/execute_tool', methods=['POST'])
def execute_tool():
    """Executes a tool based on the provided tool name and arguments."""
    try:
        data = request.get_json()
        tool_name = data.get("tool_name")
        tool_arguments = data.get("arguments", {})

        if not tool_name:
            return jsonify({"success": False, "error": "Tool name is required"}), 400

        if tool_name in TOOL_MAPPING:
            function_, _ = TOOL_MAPPING[tool_name]
            try:
                result = function_(tool_arguments.get("param", {}), tool_arguments.get("data", {}))
                if 'error' in result:
                    return jsonify({"result": result['error'], "success": False})
                return jsonify({"result": result, "success": True})
            except Exception as e:
                return jsonify({"result": str(e), "success": False})
        
        return jsonify({"success": False, "result": "No matching tool found"}), 400

    except Exception as e:
        return jsonify({"success": False, "result": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
