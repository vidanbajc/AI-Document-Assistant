import sys
from src.logger import logging
from src.exception import CustomException
from src.components.llm import get_llm
from src.components.embeddings import get_embeddings_model
from src.components.vector_store import VectorStore
from src.prompts.prompt_template import get_prompt_template
from dataclasses import dataclass
from src.services.retriever import Retriever
from src.services.answer_generator import AnswerGenerator
from src.utils import get_sources

@dataclass
class RAGPipeline:
    def query(self, question: str):
        try:
            logging.info(f"Processing query: {question}")

            retriever = Retriever()
            documents, metadatas = retriever.retrieve(question)
            
            response = AnswerGenerator()
            for chunk in response.generate(question, documents):
                yield chunk

            sources = get_sources(metadatas)

            yield "\n\nSources:\n"
            for source in sources:
                yield f"- {source}\n"

        except Exception as e:
            logging.error("Could not process query.")
            raise CustomException(e, sys)


pipeline = RAGPipeline()
question = input("Ask: ")

for token in pipeline.query(question):
    print(token, end="", flush=True)

print()