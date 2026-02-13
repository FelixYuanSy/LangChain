from itertools import chain
from typing import Union

from google import genai
from google.genai import types
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     config=types.GenerateContentConfig(
#         system_instruction = "you are my study and life leader"
#     ),
#     contents="could you tell me who you are?"
#
# )
#
# # print(response)
# print("-----------------------------")
# output_text = response.text
# # print(output_text)
# chain = response | output_text
# print(chain)

llm = ChatGoogleGenerativeAI(model ="gemini-3-flash-preview",temperature = 2 )
# prompt = ChatPromptTemplate.from_template("You are my study and life leader,please answer {topic} question")
# chain = prompt | llm | StrOutputParser()
messages = [
    SystemMessage(content="请发挥想象进行词语填空"),
    HumanMessage(content="我他妈的___")
]
# response = chain.invoke({"topic":"advantages of LangChain "})
parse = StrOutputParser()
chain = llm | parse
print(chain.invoke(messages))