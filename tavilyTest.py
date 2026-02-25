from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch


model = init_chat_model("google_genai:gemini-2.5-flash")
tool = TavilySearch()
model_with_tools = model.bind_tools(tool)
messages = [
    HumanMessage("today weather of the HangZhou")
]
ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)
for tool_call in ai_msg.tool_calls:
     tool_msg = tool.invoke(tool_call)
     messages.append(tool_msg)
print(model.invoke(messages).content)
# for tool in ai_msg.tools: