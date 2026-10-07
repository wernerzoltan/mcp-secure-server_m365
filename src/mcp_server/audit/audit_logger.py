"""
What This Interface Does: 
It defines the audit logging contract for the MCP system.

    Capability 1 – Access Logging
        2026-10-07 11:00:00
        USER=john
        RESOURCE=confluence://spaces
        ACTION=READ
        OUTCOME=ALLOWED

    Capability 2 – Error Logging
        2026-10-07 11:01:00
        USER=john
        OPERATION=search
        ERROR=invalid token
"""

from abc import ABC
from abc import abstractmethod


class AuditLogger(ABC):
    """
    Contract for audit logging.

    All audit logging implementations
    must implement this interface.
    """

    @abstractmethod
    async def log_access(
        self,
        user_id: str,
        resource: str,
        action: str,
        outcome: str,
    ) -> None:
        """
        Record an access event.

        Example:

        user_id="zwerner"
        resource="confluence://spaces"
        action="READ"
        outcome="ALLOWED"
        """
        raise NotImplementedError

    @abstractmethod
    async def log_error(
        self,
        user_id: str,
        operation: str,
        error_message: str,
    ) -> None:
        """
        Record an application error.
        """
        raise NotImplementedError