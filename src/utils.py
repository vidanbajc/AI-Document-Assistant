import sys
from src.logger import logging
from src.exception import CustomException

def get_sources(metadatas: list) -> list[str]:
    try:
        logging.info("Finding sources...")
        sources = []

        for meta in metadatas:
            source = meta.get("source", "Unknown")
            page = meta.get("page")

            if page is not None:
                sources.append(f"{source} (page {page})")
            else:
                sources.append(source)

        sources = set(sources)

        return list(sources)

    except Exception as e:
        logging.error("Failed to format document sources!")
        raise CustomException(e, sys)