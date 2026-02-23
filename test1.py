from itertools import chain
from typing import Union

from google import genai
from google.genai import types
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model

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

# llm = ChatGoogleGenerativeAI(model ="gemini-3-flash-preview",temperature = 2 )
model = init_chat_model(
    model = "google_genai:gemini-2.5-flash-lite",
    temperature = 0.3,
    max_tokens = 100,
    configurable_fields=("max_tokens",),#可配置字段
    config_prefix="first",#这是一个头字段，可以在invoke里配置

)
# prompt = ChatPromptTemplate.from_template("You are my study and life leader,please answer {topic} question")
# chain = prompt | llm | StrOutputParser()
messages = [
    SystemMessage(content="请发挥想象进行词语填空100字"),
    HumanMessage(content="我想当一个___")
]
result = model.invoke(
    messages,
    config = {
        "configurable":{"first_max_tokens":10},
    }
)
# response = chain.invoke({"topic":"advantages of LangChain "})
# parse = StrOutputParser()
# chain = llm | parse
print(result.content)