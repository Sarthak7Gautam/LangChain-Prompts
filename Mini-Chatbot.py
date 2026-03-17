from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=1.5, max_tokens=200)

chat_history = [
    SystemMessage(content='Answer the every question asked by Human in short crisp and factual way')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print('AI: ',result.content)

print(chat_history)




