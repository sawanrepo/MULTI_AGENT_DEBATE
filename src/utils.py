import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

def call_llm(prompt: str) -> str:
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content.strip()
    except Exception as e:
        return f"[Error from Gemini: {e}]"

if __name__ == "__main__":
    test_prompt = "What is the capital of France?"
    response = call_llm(test_prompt)
    print(f"LLM Response: {response}")