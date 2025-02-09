from openai import OpenAI
import json
from collection.ConfigArchive import ConfigArchive,config_archive_tools
from collection.ConnectionMetadata import ConnectionMetabody,connection_meta_tools

client = OpenAI()




function_map = {
    "import_config": ConfigArchive.import_config,
    "export_config": ConfigArchive.export_config,
    "convert_metabody":ConnectionMetabody.convert_metabody,
    "export_metabody":ConnectionMetabody.export_metabody
}


 
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

    return tool_call



tool_calls = ask_gpt('import config')


if tool_calls:
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        tool_arguments = json.loads(tool_call.function.arguments)    
        # Dynamically call the appropriate function
        if tool_name in function_map:
            print("tool name : ",tool_name)
            result = function_map[tool_name](**tool_arguments)  # Call the mapped function with arguments
        else:
            print(f"Function '{tool_name}' is not implemented.")