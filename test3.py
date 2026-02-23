from typing import Annotated

from langchain.chat_models import init_chat_model
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

model = init_chat_model("google_genai:gemini-2.5-flash-lite")
tools=[add,multiply]
model_with_tools = model.bind_tools(tools,tool_choice="any")#tool_choice强制绑定
print(model_with_tools.invoke("who are you"))