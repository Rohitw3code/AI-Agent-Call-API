import streamlit as st
import json
from openai import OpenAI
from collection.ConfigArchive import ConfigArchive, config_archive_tools
from collection.ConnectionMetadata import ConnectionMetabody, connection_meta_tools

client = OpenAI()

function_map = {
    "import_config": [ConfigArchive, ConfigArchive.import_config, ConfigArchive.import_config_data],
    "export_config": [ConfigArchive, ConfigArchive.export_config, ConfigArchive.export_config_data],
    "convert_metabody": [ConnectionMetabody, ConnectionMetabody.convert_metabody, ConnectionMetabody.convert_metabody_data],
    "export_metabody": [ConnectionMetabody, ConnectionMetabody.export_metabody, ConnectionMetabody.export_metabody_data]
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

st.title("AI-Powered Tool Executor")
user_input = st.text_input("Enter your command:")

if user_input:
    tool_calls = ask_gpt(user_input)
    
    if tool_calls:
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            tool_arguments = json.loads(tool_call.function.arguments)
            
            if tool_name in function_map:
                class_name, function, meta_data = function_map[tool_name]
                
                st.subheader(f"Function: {tool_name}")
                st.json(meta_data)
                
                if st.button(f"Execute {tool_name}"):
                    result = function(**tool_arguments)
                    st.success(f"Executed {tool_name} successfully")
                else:
                    st.warning(f"Execution of {tool_name} was not authorized.")
            else:
                st.error(f"Function '{tool_name}' is not implemented.")