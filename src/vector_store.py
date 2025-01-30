import faiss
import pinecone
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
USE_PINECONE = os.getenv("USE_PINECONE", "False").lower() == "true"

embed_model = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

class VectorDB:
    def __init__(self):
        if USE_PINECONE:
            pinecone.init(api_key=PINECONE_API_KEY, environment="us-west1-gcp")
            self.index = pinecone.Index("rag-chatbot")
        else:
            self.index = faiss.IndexFlatL2(1536)  # OpenAI's embedding size

    def add_documents(self, texts):
        vectors = [embed_model.embed(text) for text in texts]
        if USE_PINECONE:
            ids = [str(i) for i in range(len(vectors))]
            self.index.upsert(vectors=list(zip(ids, vectors)))
        else:
            self.index.add(vectors)

    def search(self, query):
        query_vector = embed_model.embed(query)
        if USE_PINECONE:
            return self.index.query(query_vector, top_k=1, include_metadata=True)
        else:
            _, I = self.index.search([query_vector], k=1)
            return I[0]

vector_db = VectorDB()
