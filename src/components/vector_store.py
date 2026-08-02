import sys
from src.exception import CustomException
from src.logger import logging
from db.connection import get_collection
from src.components.embeddings import get_embeddings_model
from dataclasses import dataclass

@dataclass
class VectorStore:
    collection = get_collection()
    embeddings = get_embeddings_model()

    def add_documents(self, ids, embeddings, documents, metadatas):
        try:
            logging.info("Adding documents to vector store.")

            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )

            logging.info("Added documents successfully.")

        except Exception as e:
            logging.error(f"Could not add documents!")
            raise CustomException(e, sys)

    def search(self, embedding, k=3):
        try:
            logging.info("Searching vector store.")

            return self.collection.query(
                query_embeddings=[embedding],
                n_results=k,
            )

        except Exception as e:
            logging.error(f"Could not search vector store!")
            raise CustomException(e, sys)

    def delete(self, ids):
        try:
            logging.info("Deleting documents from vector store.")

            self.collection.delete(ids=ids)

            logging.info("Deleted documents successfully.")

        except Exception as e:
            logging.error(f"Could not delete documents!")
            raise CustomException(e, sys)