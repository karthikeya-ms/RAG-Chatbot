from src.vector_store import vector_db
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.5)

def get_response(query):
    retrieved_doc = vector_db.search(query)
    prompt = f"Context: {retrieved_doc}\n\nAnswer the question: {query}"
    response = llm.complete(prompt)
    return response.text.strip()

if __name__ == "__main__":
    query = input("Ask a question: ")
    print(get_response(query))