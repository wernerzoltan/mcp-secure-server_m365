import logging

from mcp_server.utils.logging_config import (
    get_logger,
)


def test_logger_creation():
    logger = get_logger("test")

    assert logger is not None


def test_logger_type():
    logger = get_logger("test")

    assert isinstance(
        logger,
        logging.Logger,
    )