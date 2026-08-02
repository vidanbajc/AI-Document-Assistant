import sys
from src.exception import CustomException
from src.logger import logging
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_embeddings_model() -> GoogleGenerativeAIEmbeddings:
    try:
        logging.info("Initializing embeddings model.")

        model = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001"
        )

        logging.info("Embeddings model initialized.")
        return model

    except Exception as e:
        logging.error(f"Could not initialize embeddings model!")
        raise CustomException(e, sys)