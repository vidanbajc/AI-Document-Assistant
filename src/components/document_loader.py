from langchain_core.documents import Document
from langchain_pymupdf4llm import PyMuPDF4LLMLoader

def load_pdf(file_path: str) -> list[Document]:
    loader = PyMuPDF4LLMLoader(
        file_path=file_path, 
        mode="page", 
        extract_images=True
    )
    documents = loader.load()

    return documents