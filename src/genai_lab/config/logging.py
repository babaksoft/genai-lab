import logging

from genai_lab.config import settings


def configure_logging() -> None:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter(
            "[%(name)s] [%(levelname)s] [%(module)s:%(lineno)d] %(message)s",
        )
    )

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        handlers=[console_handler],
    )
