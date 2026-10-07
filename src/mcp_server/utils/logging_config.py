import logging

from mcp_server.config import settings


def configure_logging() -> None:
    """
    Configure application logging.
    """

    log_level = getattr(
        logging,
        settings.log_level.upper(),
        logging.INFO,
    )

    logging.basicConfig(
        level=log_level,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
    )


def get_logger(
    name: str,
) -> logging.Logger:
    """
    Return logger instance.
    """

    return logging.getLogger(name)