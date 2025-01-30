from fastapi import FastAPI
from pydantic import BaseModel
from src.chatbot import chat_with_rag

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/chat/")
async def chat(request: QueryRequest):
    response = chat_with_rag(request.question)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
