from mcp_server.audit.audit_logger import (
    AuditLogger,
)


def test_interface_exists():
    assert AuditLogger is not None


def test_has_log_access():
    assert hasattr(
        AuditLogger,
        "log_access",
    )


def test_has_log_error():
    assert hasattr(
        AuditLogger,
        "log_error",
    )