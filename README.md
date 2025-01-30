# RAG Chatbot with LangChain & FastAPI

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built using **FAISS, Pinecone, LangChain, and FastAPI**. It retrieves relevant knowledge from a database before answering queries using a **Large Language Model (LLM)**.

## 🚀 Features
- **Retrieval-Augmented Generation** (RAG) chatbot with context-aware responses.
- **Vector Search** using **FAISS or Pinecone** for efficient document retrieval.
- **LLM-based Answer Generation** using **LangChain & OpenAI API**.
- **Persistent Memory** for multi-turn conversations.
- **FastAPI Backend** for seamless API integration.
- **Dockerized** for easy deployment.
- **CI/CD Pipeline** for automated deployment.

## 📂 Project Structure
```
rag_chatbot/
│── data/                          # Folder for text documents
│   ├── sample1.txt                
│   ├── sample2.txt                 
│── models/                        
│   ├── faiss_index                 
│── src/
│   ├── ingest.py                   # Preprocess & index documents
│   ├── query.py                    # Retrieve answers from indexed docs
│   ├── chatbot.py                   # Chatbot logic with memory
│   ├── vector_store.py              # Handles FAISS / Pinecone DB
│── app.py                          # FastAPI backend
│── docker/                         
│   ├── Dockerfile                   # Docker containerization
│── tests/                          
│   ├── test_chatbot.py              # Unit tests
│── requirements.txt                
│── README.md                       
│── .github/workflows/ci_cd.yaml     # CI/CD pipeline for auto-deployments
```

## 🛠️ Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rag_chatbot.git
   cd rag_chatbot
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables**  
   Create a `.env` file and add:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   USE_PINECONE=False
   ```

## 🔧 Usage
### 1️⃣ Process Documents
```bash
python src/ingest.py
```
### 2️⃣ Start API Server
```bash
python app.py
```
### 3️⃣ Query the Chatbot
```bash
curl -X 'POST' 'http://127.0.0.1:8000/chat/' -H 'Content-Type: application/json' -d '{"question": "What is Tesla known for?"}'
```

## 🚀 Deploy with Docker
1. **Build the Docker image**
   ```bash
   docker build -t rag-chatbot .
   ```
2. **Run the container**
   ```bash
   docker run -p 8000:8000 rag-chatbot
   ```

## ✅ Running CI/CD Pipeline
The project includes **GitHub Actions CI/CD** for automated testing & deployment.
- Workflow defined in `.github/workflows/ci_cd.yaml`
- **Runs tests & builds Docker image automatically** on push.

## 🎯 Future Enhancements
- UI Integration (Streamlit/Gradio)
- Multi-document Retrieval
- Optimized Model Fine-Tuning

## 📜 License
This project is licensed under **MIT License**.
