import sys
from src.logger import logging
from src.exception import CustomException
from src.components.llm import get_llm
from src.components.embeddings import get_embeddings_model
from src.components.vector_store import VectorStore
from src.prompts.prompt_template import get_prompt_template
from dataclasses import dataclass

@dataclass
class QueryPipeline:
    llm = get_llm()
    embeddings_model = get_embeddings_model()
    vector_store = VectorStore()
    prompt = get_prompt_template()


    def query(self, question: str):
        try:
            logging.info(f"Processing query: {question}")

            embedding = self.embeddings_model.embed_query(question)

            results = self.vector_store.search(
                embedding=embedding,
                k=3
            )

            documents = results["documents"][0]
            context = "\n\n".join(documents)

            prompt = self.prompt.format(
                context=context,
                question=question
            )

            for chunk in self.llm.stream(prompt):
                if chunk.text:
                    yield chunk.text

        except Exception as e:
            logging.error("Could not process query.")
            raise CustomException(e, sys)


# pipeline = QueryPipeline()
# question = input("Ask: ")

# for token in pipeline.query(question):
#     print(token, end="", flush=True)

# print()