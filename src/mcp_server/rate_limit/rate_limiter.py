"""
What This Interface Does: 
It defines the request rate limiting contract for the MCP system.
    Capability 1: Check whether a request is allowed.
        allowed = await rate_limiter.is_allowed(
            user_id="john"
        ) 
        Result: true / false

    Capability 2: Record a successful request.
        await rate_limiter.record_request(
            user_id="john"
        )
        The implementation can decide how the request is counted. Examples:
            in-memory counter
            Redis
            database
            distributed cache
"""

from abc import ABC
from abc import abstractmethod


class RateLimiter(ABC):
    """
    Contract for request rate limiting.
    """

    @abstractmethod
    async def is_allowed(
        self,
        user_id: str,
    ) -> bool:
        """
        Check whether the user is allowed
        to perform another request.

        Returns:
            True if request is allowed
            False otherwise
        """
        raise NotImplementedError

    @abstractmethod
    async def record_request(
        self,
        user_id: str,
    ) -> None:
        """
        Record a successful request.
        """
        raise NotImplementedError
