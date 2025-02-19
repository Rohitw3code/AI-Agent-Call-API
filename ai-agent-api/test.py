from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationSummaryMemory
from tool_mapping import TOOL_MAPPING
from collection.ConfigArchive import config_archive_tools
from collection.ConnectionMetadata import connection_meta_tools
from langchain_core.messages import HumanMessage, SystemMessage
import json

# Initialize model with tools
llm = ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000)
all_tools = config_archive_tools + connection_meta_tools
llm_with_tools = llm.bind_tools(all_tools)

# Initialize conversation memory with updated method
memory = ConversationSummaryMemory(llm=llm)

def process_query(query):
    # Load conversation history
    history = memory.load_memory_variables({})['history']
    messages = []
    
    if history:
        messages.append(SystemMessage(content=f"Conversation context: {history}"))
    messages.append(HumanMessage(content=query))
    
    # Get model response
    response = llm_with_tools.invoke(messages)
    
    # Process tool calls
    tool_responses = []
    tool_calls = response.additional_kwargs.get("tool_calls", [])
    print("tool_calls : ", tool_calls)
    for call in tool_calls:
        func_name = call['function']['name']
        args = json.loads(call['function']['arguments'])
        
        if func_name in TOOL_MAPPING:
            try:
                tool_func = TOOL_MAPPING[func_name][0]
                # Proper invocation with arguments
                result = tool_func.invoke(input=args)
                print("result : ", result)
                tool_responses.append(f"{func_name} executed. Result: {result}")
            except Exception as e:
                tool_responses.append(f"Error executing {func_name}: {str(e)}")
        else:
            tool_responses.append(f"Tool {func_name} not found")
    
    final_response = "\n".join(tool_responses) if tool_responses else response.content
    
    # Update memory
    memory.save_context({"input": query}, {"output": final_response})
    
    return final_response

# Default query execution
default_query = "import config"
print("Processing default query:", default_query)
first_response = process_query(default_query)
print("Response:", first_response)

# Demonstrate memory retention
follow_up = "What did I ask about previously?"
print("\nFollow-up query:", follow_up)
follow_up_response = process_query(follow_up)
print("Memory-based response:", follow_up_response)

# Show final memory state
print("\nConversation Summary:")
print(memory.buffer)