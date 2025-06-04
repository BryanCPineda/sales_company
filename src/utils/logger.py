import logging
from colorlog import ColoredFormatter

def get_logger(name: str) -> logging.Logger:
    """
    Crea y configura un logger con formato de color.
    Args:
        name (str): Nombre del logger.
    Returns:
        logging.Logger: Logger configurado con formato de color.
    """
    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False 

    return logger