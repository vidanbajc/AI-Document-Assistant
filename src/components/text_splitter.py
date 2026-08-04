import sys
from src.exception import CustomException
from src.logger import logging
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents: list[Document]) -> list[Document]:
    try:
        logging.info("Splitting documents.")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

        logging.info("Documents split successfully.")
        return chunks

    except Exception as e:
        logging.error(f"Could not split documents!")
        raise CustomException(e, sys)
