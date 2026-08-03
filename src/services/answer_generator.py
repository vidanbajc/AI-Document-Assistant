import sys
from src.logger import logging
from src.exception import CustomException
from src.components.llm import get_llm
from src.prompts.prompt_template import get_prompt_template
from dataclasses import dataclass

@dataclass
class AnswerGenerator:
    llm = get_llm()
    prompt = get_prompt_template()

    def generate(self, question, documents):
        try:
            logging.info(f"Generating response...")

            context = "\n\n".join(documents)

            prompt = self.prompt.format(
                context=context,
                question=question
            )

            for chunk in self.llm.stream(prompt):
                if chunk.text:
                    yield chunk.text

        except Exception as e:
            logging.error("Failed to generate answer.")
            raise CustomException(e, sys)