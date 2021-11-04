import logging
import logging.handlers
from logging.config import dictConfig

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}


def configure_logging(name):
    """
    Initialize logging defaults for Project.

    :param logfile_path: logfile used to the logfile
    :type logfile_path: string

    This function does:

    - Assign INFO and DEBUG level to logger file handler and console handler

    """
    logger = logging.getLogger(name)

    dictConfig(DEFAULT_LOGGING)

    default_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] [PID:%(process)d TID:%(thread)d] %(message)s",
        "%d/%m/%Y %H:%M:%S")
    # file handler
    # file_handler = logging.handlers.RotatingFileHandler("app/logger/logger_info.log", maxBytes=5000,backupCount=20, encoding='utf-8')
    # file_handler.setLevel(logging.INFO)

    # file handler
    # console_handler = logging.StreamHandler()
    console_handler = logging.handlers.RotatingFileHandler("app/logger/logger.log", maxBytes=500000, backupCount=1,
                                                           encoding='utf-8')
    console_handler.setLevel(logging.DEBUG)
    # file_handler.setFormatter(default_formatter)
    console_handler.setFormatter(default_formatter)

    # logging.root.setLevel(logging.DEBUG)
    # logging.root.addHandler(file_handler)
    # logging.root.addHandler(console_handler)

    logger.root.setLevel(logging.DEBUG)
    # logger.root.addHandler(file_handler)
    # logger.root.addHandler(console_handler)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(console_handler)
    # logger.addHandler(console_handler)

    return logger
