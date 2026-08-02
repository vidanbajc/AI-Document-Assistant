import os
import sys
from src.exception import CustomException
from src.logger import logging
from langchain_core.documents import Document
from langchain_pymupdf4llm import PyMuPDF4LLMLoader

def load_pdf(file_path: str) -> list[Document]:
    try:
        logging.info(f"Loading PDF: {file_path}")

        loader = PyMuPDF4LLMLoader(
            file_path=file_path,
            mode="page",
            extract_images=False
        )

        documents = loader.load()

        logging.info("PDF loaded successfully.")
        return documents

    except Exception as e:
        logging.error(f"Could not load PDF!")
        raise CustomException(e, sys)


def load_documents(folder_path: str) -> list[Document]:
    try:
        logging.info(f"Loading documents from: {folder_path}")

        all_documents = []

        for file_name in os.listdir(folder_path):
            if file_name.endswith(".pdf"):
                file_path = os.path.join(folder_path, file_name)

                documents = load_pdf(file_path)
                all_documents.extend(documents)

        if not all_documents:
            raise

        logging.info(f"Loaded {len(all_documents)} document pages.")
        return all_documents

    except Exception as e:
        logging.error(f"Could not load documents!")
        raise CustomException(e, sys)