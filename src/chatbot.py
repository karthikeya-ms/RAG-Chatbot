from src.vector_store import vector_db
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=OPENAI_API_KEY)
memory = ConversationBufferMemory(memory_key="chat_history")

def chat_with_rag(query):
    retrieved_doc = vector_db.search(query)
    chain = ConversationalRetrievalChain(
        llm=llm,
        retriever=retrieved_doc,
        memory=memory
    )
    response = chain.run(query)
    return response

if __name__ == "__main__":
    while True:
        query = input("You: ")
        print("AI:", chat_with_rag(query))
