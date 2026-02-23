from typing import Tuple, List

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class AddInput(BaseModel):
	a:int = Field(description = "第一个整数")
	b:int = Field(description = "第二个整数")

def add(a:int,b:int)->Tuple[str,List[int]]:
    nums = [a,b]
    content = f"{nums}相加的结果是{a+b}"
    return content, nums

add_tool = StructuredTool.from_function(
	func=add,
	name="ADD",#工具名
	description="两数相加", #工具描述
	args_schema=AddInput ,#参数描述
	response_format="content_and_artifact" #展示过程
)
# print(add_tool.invoke({"a":2,"b":5})) #这样调用不显示response_fomat
tools = []
print(add_tool.invoke(
	{
		"name":"ADD",
		"args":{"a":3,"b":5},
		"type":"tool_call",
		"id":"111", #用于奖工具调用请求和结果关联
	}
))