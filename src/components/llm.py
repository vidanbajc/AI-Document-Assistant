import sys
from src.logger import logging
from src.exception import CustomException
from config import GOOGLE_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm() -> ChatGoogleGenerativeAI:
    try:
          
        logging.info("Loading Google Gemini...")

        llm = ChatGoogleGenerativeAI(
            model="gemini-3.6-flash", # gemini-flash-latest
            google_api_key=GOOGLE_API_KEY,
            #temperature=0.1, # gemini-3.6-flash is not supporting temperature parameter
            thinking_level="low",
            max_retries=1
        )

        logging.info("Gemini loaded successfully.")

        return llm

    except Exception as e:
        logging.error(f"Failed to load Gemini!")
        raise CustomException(e, sys)