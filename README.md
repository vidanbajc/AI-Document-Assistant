# AI-Document-Assistant

End-to-end **Retrieval Augmented Generation (RAG)** application that allows users to ask questions about a documents using natural language.  
The system processes PDF documents, stores their vector representations in **ChromaDB**, retrieves the most relevant context for each query and generates accurate answers using a Large Language Model (LLM).

---

## 📌 Problem Statement

LLM cannot reliably answer questions about information that is not included in their training data or explicitly provided during inference.

This project solves that by implementing a Retrieval Augmented Generation (RAG) pipeline that retrieves the most relevant document chunks from a vector database and uses them as context for the LLM.  
The generated answers are based exclusively on the ingested PDF documents, ensuring responses rely only on the available knowledge rather than the model's own assumptions.

---

## 📄 Documents

* Documents are provided as PDF files.
* PDFs are loaded and converted into text.
* Documents are split into overlapping chunks.
* Each chunk is transformed into a vector embedding.
* Embeddings are stored in ChromaDB for semantic retrieval.

---

## 🏗️ Project Structure

```bash
AI-Document-Assistant/
│
├── app/
│   ├── backend/
│   │   └── main.py              # FastAPI application
│   │
│   └── frontend/
│       └── templates/           # HTML frontend (Bootstrap)
│           
├── data/
│   └── PDF/                     # Original uploaded PDFs
│
├── db/
│   └── connection.py            # ChromaDB initialization
│
├── docker/
│   ├── chromadb/
│   │   └── docker-compose.yml   # Starts the ChromaDB container
│   └── Dockerfile               # Docker image for the FastAPI application
│
├── logs/                         # Logging files
│
├── src/
│   ├── components/
│   │   ├── document_loader.py    # Loads PDF documents
│   │   ├── text_splitter.py      # Splits documents into chunks
│   │   ├── embeddings.py         # Embedding model initialization
│   │   ├── vector_store.py       # ChromaDB operations
│   │   └── llm.py                # LLM initialization
│   │
│   ├── pipeline/
│   │   ├── ingestion_pipeline.py # Load → Split → Embed → Store
│   │   └── rag_pipeline.py       # Retrieve → Prompt → Generate
│   │
│   ├── prompts/
│   │   └── prompt_template.py    # Prompt template used by the RAG pipeline
│   │
│   ├── services/
│   │   ├── answer_generator.py   # Generates responses
│   │   └── retriever.py          # Retrieves relevant document chunks
│   │
│   ├── utils.py                  # Utility functions
│   ├── logger.py                 # Logging configuration
│   └── exception.py              # Custom exception handling
│
├── config.py                     # Environment variables (.env)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ RAG Pipeline

### The project follows a complete RAG workflow:

1. Load PDF documents.
2. Split documents into overlapping text chunks.
3. Generate embeddings for every chunk.
4. Store embeddings inside ChromaDB.
5. Embed the user's question.
6. Retrieve the most relevant document chunks.
7. Build a prompt containing the retrieved context.
8. Generate the final answer using the LLM.
9. Stream the response back to the user.

---

## 🤖 Technologies Used

* LangChain
* ChromaDB
* FastAPI
* Docker
* Google Gemini
* Google Embedding Model

---

## 🚀 Deployment

The application is containerized using Docker.  
Docker is used to run the ChromaDB server, while the FastAPI application is packaged into its own Docker image.

---

## ▶️ How to Run

**Important:** Before starting the application, execute the ingestion pipeline to process your PDF documents and populate the ChromaDB collection. 

### Prerequisites
Make sure you have installed:
* Docker
* Docker Desktop

### Clone the repository:
```bash
git clone https://github.com/vidanbajc/AI-Document-Assistant.git
cd AI-Document-Assistant
```

### Create a .env file in the root directory:
```bash
GOOGLE_API_KEY=your_api_key_here

CHROMA_HOST=chroma
CHROMA_PORT=8000
CHROMA_COLLECTION=your_collection_name
```

### Navigate to the ChromaDB Docker folder and start:
```bash
cd docker/chromadb
docker compose up -d
```

### Create Docker network and Connect the ChromaDB container:
```bash
docker network create ai-docs-network
docker network connect ai-docs-network chroma
```

### Return to the project root and build the application image:
```bash
cd ../..
docker build -t ai-document-assistant .
```

### Run the application
```bash
docker run --name app --network ai-docs-network --env-file .env -p 8000:8000 ai-document-assistant
```

### Stop the application
```bash
docker stop app

cd docker/chromadb
docker compose down
```

---

## 🔮 Future Improvements

* Support multiple document formats (DOCX, TXT, Markdown...)
* Hybrid search (semantic + keyword)
* Cloud deployment

---

## 👤 Author

* Name: Vidan Bajc
* Email: <vidanbajc@gmail.com>