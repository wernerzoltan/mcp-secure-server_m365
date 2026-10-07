"""
What This Interface Does:
Capability 1: Retrieve a secret.
    Example future usage:
        client_secret = await secret_store.get_secret(
            "okta-client-secret"
        )
    The caller does not care whether the value comes from:
    - Mock storage
    - Azure Key Vault
    - Other secure stores

Capability 2: Check if a secret exists.
    Example future usage:
        if not await secret_store.secret_exists(
            "confluence-api-token"
        )
"""


from abc import ABC
from abc import abstractmethod


class SecretStore(ABC):
    """
    Contract for secret management.

    Implementations may use:

    - Mock in-memory storage
    - Azure Key Vault
    - Other secure stores

    The rest of the application
    depends only on this interface.
    """

    @abstractmethod
    async def get_secret(
        self,
        secret_name: str
    ) -> str:
        """
        Retrieve a secret value.

        Args:
            secret_name: Secret identifier

        Returns:
            Secret value
        """
        raise NotImplementedError

    @abstractmethod
    async def secret_exists(
        self,
        secret_name: str
    ) -> bool:
        """
        Check whether a secret exists.

        Args:
            secret_name: Secret identifier

        Returns:
            True if secret exists
            False otherwise
        """
        raise NotImplementedError

    @abstractmethod
    async def set_secret(
        self,
        secret_name: str,
        secret_value: str,
    ) -> None:
        """
        Create or update a secret.
        """
        raise NotImplementedError