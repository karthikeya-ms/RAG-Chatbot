import os
from src.vector_store import vector_db

def load_documents():
    texts = []
    for filename in os.listdir("data"):
        with open(os.path.join("data", filename), "r") as file:
            texts.append(file.read())
    return texts

if __name__ == "__main__":
    documents = load_documents()
    vector_db.add_documents(documents)
    print("Documents processed and stored in the vector database.")