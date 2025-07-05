from langchain.chat_models import ChatCohere
from langchain.schema import HumanMessage
import os


# Set your API key  
COHERE_API_KEY = os.getenv("COHERE_API_KEY") or "W0ZMiF8D4eU3eMGgZevXJMPwnJMzJVtd7JYwvo0V"

chat_model = ChatCohere(
    cohere_api_key=COHERE_API_KEY,
    model="command-r",
    temperature=0.6
)

def get_bot_reply(user_message: str) -> str:
    try:
        # Proper way in LangChain >= 0.1.7
        response = chat_model.invoke([HumanMessage(content=user_message)])
        return response.content  # ✅ No token_count used
    except Exception as e:
        return f"⚠️ Error: {e}"

