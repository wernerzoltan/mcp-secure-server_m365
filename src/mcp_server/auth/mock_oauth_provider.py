"""
What This Code Does:
    Provides a mock implementation of an OAuth provider for development purposes.
    It simulates token validation and user identity retrieval without connecting to a real Okta server.
    This is useful for testing and development environments where a real OAuth provider is not available.
    Valid token: mock-valid-token
    Returns mock user identity for a valid token.
    Invalid token: mock-invalid-token raises ValueError.
    Example usage:
        provider = MockOAuthProvider()
        await provider.validate_token("mock-valid-token")  # True
        await provider.get_user_id("mock-valid-token")    # "mock-user"
        await provider.validate_token("mock-invalid-token")  # False
        await provider.get_user_id("mock-invalid-token")    # Raises ValueError
"""
import base64
import json
import time

from mcp_server.auth.oauth_provider import (
    OAuthProvider,
)
from mcp_server.auth.mock_jwks import (
    MOCK_JWKS,
)



class MockOAuthProvider(OAuthProvider):
    """
    Mock OAuth provider.

    Development only.

    No real Okta connection.
    """


    """
    What This Code Does:
        Example:
            token = await provider.create_token(
                "john"
            )
        Provides a mock token for the given user ID:
        Example output:
            "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJqb2huIiwiZXhwIjoxNjg4NzY4MDAwfQ.mock-signature"
            Where the header contains the algorithm and type:
                {
                    "alg": "none",
                    "typ": "JWT"
                }
            Where the payload contains the user ID and expiration time:
                {
                    "sub": "john",
                    "exp": 1688768000
                }
       
    """
    async def create_token(
        self,
        user_id: str,
        expires_in_seconds: int = 3600,
    ) -> str:
        """
        Create a mock JWT-like token.
        """

        header = {
            "alg": "none",
            "typ": "JWT",
        }

        payload = {
            "sub": user_id,
            "exp": (
                int(time.time()) +
                expires_in_seconds
            ),
        }

        header_b64 = base64.urlsafe_b64encode(
            json.dumps(header).encode()
        ).decode()

        payload_b64 = base64.urlsafe_b64encode(
            json.dumps(payload).encode()
        ).decode()

        signature = "mock-signature"

        return (
            f"{header_b64}."
            f"{payload_b64}."
            f"{signature}"
        )

    async def validate_token(
        self,
        token: str,
    ) -> bool:
        """
        Validate mock JWT token.
        """

        try:
            parts = token.split(".")

            if len(parts) != 3:
                return False

            payload_b64 = parts[1]

            payload_json = (
                base64.urlsafe_b64decode(
                    payload_b64
                ).decode()
            )

            payload = json.loads(
                payload_json
            )

            if "sub" not in payload:
                return False

            if "exp" not in payload:
                return False

            current_time = int(
                time.time()
            )

            if payload["exp"] < current_time:
                return False

            return True

        except Exception:
            return False

    async def get_user_id(
        self,
        token: str,
    ) -> str:

        if not await self.validate_token(
            token
        ):
            raise ValueError(
                "Invalid token"
            )

        payload_b64 = token.split(".")[1]

        payload_json = (
            base64.urlsafe_b64decode(
                payload_b64
            ).decode()
        )

        payload = json.loads(
            payload_json
        )

        return payload["sub"]

    async def get_jwks(self) -> dict:
        """
        Return mock JWKS document.
        """

        return MOCK_JWKS