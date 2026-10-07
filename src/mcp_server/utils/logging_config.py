import logging

"""
Creates a centralized logging configuration.
Later every component will automatically follow the same logging standard.
Example output:
    2024-06-05 12:34:56 | INFO | my_module | This is an info message

"""
def configure_logging() -> None:
    """
    Configure application logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
    )


def get_logger(name: str) -> logging.Logger:
    """
    Return logger instance.
    """

    return logging.getLogger(name)