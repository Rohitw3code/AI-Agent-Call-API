from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from openai import OpenAI
from collection.ConfigArchive import ConfigArchive, config_archive_tools
from collection.ConnectionMetadata import ConnectionMetabody, connection_meta_tools

app = Flask(__name__)
CORS(app)
client = OpenAI()

# Mapping tools to functions
function_map = {
    "import_config": [ConfigArchive, ConfigArchive.import_config, ConfigArchive.import_config_data],
    "export_config": [ConfigArchive, ConfigArchive.export_config, ConfigArchive.export_config_data],
    "convert_metabody": [ConnectionMetabody, ConnectionMetabody.convert_metabody, ConnectionMetabody.convert_metabody_data],
    "export_metabody": [ConnectionMetabody, ConnectionMetabody.export_metabody, ConnectionMetabody.export_metabody_data]
}

# Collect tools
tools = []
tools.extend(config_archive_tools)
tools.extend(connection_meta_tools)

def ask_gpt(msg):
    messages = [{"role": "user", "content": msg}]
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
    )    
    tool_call = completion.choices[0].message.tool_calls

    if tool_call:
        tool_name = tool_call[0].function.name
        meta_data = function_map.get(tool_name, [None, None, None])[2]
        return {"tool_name": tool_name, "meta_data": meta_data}
    
    return {"error": "No tool call found"}

@app.route('/ask_gpt', methods=['POST'])
def handle_ask_gpt():
    data = request.get_json()
    user_query = data.get("query", "")
    response = ask_gpt(user_query)
    print("resp : ",response)
    return jsonify(response)

@app.route('/execute_tool', methods=['POST'])
def execute_tool():
    data = request.get_json()
    tool_name = data.get("tool_name")
    tool_arguments = data.get("arguments", {})
    
    if isinstance(tool_arguments, str):
        try:
            tool_arguments = json.loads(tool_arguments)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON format in arguments"})
    
    if not isinstance(tool_arguments, dict):
        return jsonify({"error": "Arguments must be a dictionary"})
    
    if tool_name in function_map:
        class_name, function, _ = function_map[tool_name]            
        print("tool argument : ",tool_arguments)
        result = function(**tool_arguments)
        return jsonify({"result": result})
    
    return jsonify({"error": "Invalid tool name"})

if __name__ == '__main__':
    app.run(debug=True)
