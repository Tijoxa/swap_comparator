import logging
import colorlog


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()

        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)s: %(message)s\n",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)


setup_logger()
