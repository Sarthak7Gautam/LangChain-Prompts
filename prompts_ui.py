from langchain_groq import ChatGroq # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile",temperature=1)

result = model.invoke('How much Api calls per day does Groq model provides?')

print(result.content)