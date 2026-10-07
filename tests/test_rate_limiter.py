from mcp_server.rate_limit.rate_limiter import (
    RateLimiter,
)


def test_interface_exists():
    assert RateLimiter is not None


def test_has_is_allowed():
    assert hasattr(
        RateLimiter,
        "is_allowed",
    )


def test_has_record_request():
    assert hasattr(
        RateLimiter,
        "record_request",
    )