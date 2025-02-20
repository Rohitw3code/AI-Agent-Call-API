from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chains.conversation.memory import ConversationSummaryMemory
from tool_mapping import TOOL_MAPPING
from collection.ConfigArchive import config_archive_tools
from collection.ConnectionMetadata import connection_meta_tools
from collection.config_tools import idp_sp_tools
import json

app = FastAPI()

# uvicorn fast_api:app --host 0.0.0.0 --port 5000 --reload 

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

# Initialize model and tools
llm = ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000)
# all_tools = config_archive_tools + connection_meta_tools
all_tools = idp_sp_tools.copy()
llm_with_tools = llm.bind_tools(all_tools)

# Initialize conversation memory
memory = ConversationSummaryMemory(llm=llm)

class QueryRequest(BaseModel):
    query: str

query = ""

class ToolExecutionRequest(BaseModel):
    tool_name: str
    arguments: dict = {}

def get_conversation_context():
    """Retrieve and format conversation history."""
    history = memory.load_memory_variables({}).get('history', '')
    messages = [SystemMessage(content=f"Conversation context: {history}")] if history else []
    return messages

@app.post("/ask_gpt")
async def ask_gpt(request: QueryRequest):
    """Processes a query through GPT-4 and returns a response."""
    global query
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query is required")
    
    print("/ask_gpt called with query:", query)
    messages = get_conversation_context() + [HumanMessage(content=query)]
    response = llm_with_tools.invoke(messages)
    
    tool_calls = response.additional_kwargs.get("tool_calls", [])
    print("tool_calls:", tool_calls)
    
    if not tool_calls:
        final_response = response.content
        print("Generated response:", final_response)
        return {"type": "ai-response", "ai": final_response}
    
    tool_name = tool_calls[0]['function']['name']
    if tool_name in TOOL_MAPPING:
        _, meta_data = TOOL_MAPPING[tool_name]
        success_message = f"{tool_name} function name received as result"
        print("Success message:", success_message)
        return {"tool_name": tool_name, "meta_data": meta_data, "type": "tool"}
    
    raise HTTPException(status_code=500, detail="Tool not found in mapping")

@app.post("/execute_tool")
async def execute_tool(request: ToolExecutionRequest):
    """Executes a tool based on the provided tool name and arguments."""
    global query
    tool_name = request.tool_name.strip()
    tool_arguments = request.arguments
    
    if not tool_name:
        raise HTTPException(status_code=400, detail="Tool name is required")
    
    print("/execute_tool called for:", tool_name)
    messages = get_conversation_context() + [HumanMessage(content=tool_name)]
    response = llm_with_tools.invoke(messages)
    
    tool_responses = []
    success = True
    
    if tool_name in TOOL_MAPPING:
        function_, _ = TOOL_MAPPING[tool_name]
        try:
            print("Invoking tool with arguments:", tool_arguments)
            result = function_.invoke(input=tool_arguments)
            print("Tool execution result:", result)
            if 'error' in result:
                success = False
            tool_responses.append(f"{tool_name} executed. Result: {result}")
        except Exception as e:
            success = False
            error_message = f"Error executing {tool_name}: {str(e)}"
            print(error_message)
            tool_responses.append(error_message)
    else:
        error_message = "No matching tool found"
        print(error_message)
        success = False
        tool_responses.append(error_message)
    
    final_response = "\n".join(tool_responses)
    memory.save_context({"input": "query : "+query}, {"output": final_response})
    
    return {"type": "result", "result": final_response, "success": success}
