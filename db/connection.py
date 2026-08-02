import sys
import chromadb
from src.exception import CustomException
from src.logger import logging
from config import CHROMA_HOST, CHROMA_PORT, CHROMA_COLLECTION

def get_collection() -> chromadb.Collection:
    try:
        logging.info("Getting collection.")

        client = chromadb.HttpClient(
            host=CHROMA_HOST,
            port=CHROMA_PORT
        )

        logging.info("Collection created successfully.")

        return client.get_or_create_collection(name = CHROMA_COLLECTION)
    
    except Exception as e:
        logging.error(f"Could not get collection!")
        raise CustomException(e,sys)
