from abc import ABC
from abc import abstractmethod
from numbers import Real
from unittest.mock import Mock
from unittest.mock import Mock


class OAuthProvider(ABC):
    """
    OAuth provider contract.

    All OAuth implementations
    must inherit from this interface.
    """

    # Future behavior: true, if token is valid
    # Later: 
    #  Mock implementation
    #   Real Okta implementation must both provide this method. 

    # Why async? Because token validation might involve network calls or other I/O operations.
    @abstractmethod
    async def validate_token(
        self,
        token: str
    ) -> bool:
        """
        Validate an access token.

        Returns:
            True if valid
            False otherwise
        """
        raise NotImplementedError

    # Return a user identity such as:
    # {
    #     "id": "123",
    #     "username": "johndoe",
    #     "email": "johndoe@example.com"
    # }
    # derived from the access token.
    @abstractmethod
    async def get_user_id(
        self,
        token: str
    ) -> str:
        """
        Extract user identity from token.
        """
        raise NotImplementedError