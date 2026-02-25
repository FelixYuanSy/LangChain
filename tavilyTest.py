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
# The weather in Hangzhou on **February 25, 2026, at 18:15 local time** is as follows:
#
# *   **Temperature:** 11.1°C (52.0°F)
# *   **Feels like:** 9.7°C (49.5°F)
# *   **Condition:** Partly cloudy
# *   **Wind:** 11.5 kph (7.2 mph) from the East
# *   **Humidity:** 76%
