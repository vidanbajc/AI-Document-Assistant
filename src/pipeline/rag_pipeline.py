import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.services.retriever import Retriever
from src.services.answer_generator import AnswerGenerator
from src.utils import get_sources

retriever = Retriever()
response = AnswerGenerator()

@dataclass
class RAGPipeline:
    def query(self, question: str):
        try:
            logging.info(f"Processing query: {question}")

            documents, metadatas = retriever.retrieve(question)
            
            for chunk in response.generate(question, documents):
                yield chunk

            sources = get_sources(metadatas)

            yield "\n\nSources:\n"
            for source in sources:
                yield f"- {source}\n"

        except Exception as e:
            logging.error("Could not process query.")
            raise CustomException(e, sys)


# pipeline = RAGPipeline()
# question = input("Ask: ")

# for token in pipeline.query(question):
#     print(token, end="", flush=True)

# print()