from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", max_tokens=100)

messages = [
    SystemMessage(content="You are a AI Engineer"),
    HumanMessage(
        content="When we have LangChain to build AI Agents then why is LangGraph used to build AI Agents"
    ),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
