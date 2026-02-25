from typing import Annotated

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool



@tool
def add(
        a:Annotated[int,...,"第一个整数"],
        b:Annotated[int,...,"第二个整数"]
)->int:
    """两数相加"""
    return a+b

@tool
def multiply(
        a: Annotated[int, ..., "第一个整数"],
        b: Annotated[int, ..., "第二个整数"]
) -> int:
    """两数相乘"""
    return a * b

model = init_chat_model("google_genai:gemini-2.5-flash")
tools=[add,multiply]
model_with_tools = model.bind_tools(tools,tool_choice="any")#tool_choice强制绑定
model_with_tools = model.bind_tools(tools)#tool_choice强制绑定
mes = [
    HumanMessage("2乘以2是多少？4加4是多少？"),
]

ai_msg = model_with_tools.invoke(mes)
mes.append(ai_msg)
for tool_call in ai_msg.tool_calls:
    select_tool = {"add":add,"multiply":multiply}[tool_call["name"].lower()]
    tool_msg = select_tool.invoke(tool_call)
    mes.append(tool_msg)
print(mes)
print(model.invoke(mes).content)