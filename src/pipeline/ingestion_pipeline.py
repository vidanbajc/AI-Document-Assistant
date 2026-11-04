import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.document_loader import load_documents
from src.components.text_splitter import split_documents
from src.components.vector_store import VectorStore

def start_pipeline():
    try:
        logging.info("Starting ingestion pipeline.")

        folder_path = os.path.join("data", "pdf")
        documents = load_documents(folder_path)
        chunks = split_documents(documents)

        vector_store = VectorStore()

        ids = [str(i) for i in range(len(chunks))]
        texts = [chunk.page_content for chunk in chunks]

        metadatas = [
            {
                "source": os.path.basename(chunk.metadata.get("source", "Unknown")),
                "page": chunk.metadata.get("page", 0) + 1
            }
            for chunk in chunks
        ]

        vector_store.delete_all()

        embeddings = vector_store.embeddings.embed_documents(texts)

        vector_store.add_documents(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )

        # results = vector_store.search(
        #     embedding=embeddings[0],
        #     k=3
        # )
        
        # print(results)

    except Exception as e:
        logging.error(f"Ingestion pipeline failed!")
        raise CustomException(e, sys)

if __name__ == "__main__":
    start_pipeline()