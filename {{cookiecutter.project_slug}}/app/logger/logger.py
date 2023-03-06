"""Define Logger for log message."""

import logging
from datetime import datetime


class UvicornFormatter(logging.Formatter):
    """Uvicorn Formatter."""

    FORMAT = (
        "\033[38;5;244m%(asctime)s\033[0m"
        " | "
        "%(levelname)-7s"
        " | "
        "\033[38;5;214m%(name)s\033[0m"
        " : "
        "\033[38;5;111m%(message)s\033[0m"
    )

    LEVEL_COLORS = {
        "DEBUG": "\033[38;5;32m",
        "INFO": "\033[38;5;36m",
        "WARNING": "\033[38;5;221m",
        "ERROR": "\033[38;5;196m",
        "CRITICAL": "\033[48;5;196;38;5;231m",
    }

    def format(self, record):
        """Config format"""
        levelname = record.levelname
        level_color = self.LEVEL_COLORS.get(levelname, "")
        record.levelname = f"{level_color}{levelname}\033[0m"
        record.asctime = datetime.fromtimestamp(record.created).strftime("%Y-%m-%d %H:%M:%S.%f")
        return super().format(record)


def configure_logging():
    """Initialize logging defaults for Project.

    This function does:
    - Assign INFO and DEBUG level to logger file handler and console handler.

    Returns:
        Logger.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler with a lower log level
    file_handler = logging.FileHandler('app/logger/logger.log')
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handlers
    default_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] "
        "[%(funcName)s():%(lineno)s] [PID:%(process)d TID:%(thread)d] %(message)s",
        "%d/%m/%Y %H:%M:%S")

    file_handler.setFormatter(default_formatter)
    console_handler.setFormatter(UvicornFormatter(UvicornFormatter.FORMAT))

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


custom_logger = configure_logging()
