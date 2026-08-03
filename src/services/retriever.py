import sys
from src.logger import logging
from src.exception import CustomException
from src.components.embeddings import get_embeddings_model
from src.components.vector_store import VectorStore
from dataclasses import dataclass

@dataclass
class Retriever:
    embeddings_model = get_embeddings_model()
    vector_store = VectorStore()

    def retrieve(self, question: str):
        try:
            logging.info(f"Processing query: {question}")

            embedding = self.embeddings_model.embed_query(question)

            results = self.vector_store.search(
                embedding=embedding,
                k=3
            )

            documents = results["documents"][0]
            metadatas = results["metadatas"][0]

            return documents, metadatas

        except Exception as e:
            logging.error("Failed to retrieve documents from vector store.")
            raise CustomException(e, sys)