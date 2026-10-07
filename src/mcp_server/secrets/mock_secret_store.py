from mcp_server.secrets.secret_store import (
    SecretStore,
)
from datetime import datetime
from mcp_server.secrets.models import (
    SecretMetadata,
    SecretRecord,
)



class MockSecretStore(SecretStore):
    """
    Mock secret store.

    Development only.

    Uses in-memory storage.
    """

    def __init__(self) -> None:
        self._secrets: dict[
            str,
            list[SecretRecord]
        ] = {
            "okta-client-id": [
                SecretRecord(
                    value="mock-client-id",
                    version=1,
                )
            ],
            "okta-client-secret": [
                SecretRecord(
                    value="mock-client-secret",
                    version=1,
                )
            ],
            "confluence-api-token": [
                SecretRecord(
                    value="mock-confluence-token",
                    version=1,
                )
            ],
        }

        self._metadata: dict[
            str,
            SecretMetadata,
        ] = {
            "okta-client-id": SecretMetadata(
                rotation_count=0,
                last_rotated=None,
            ),
            "okta-client-secret": SecretMetadata(
                rotation_count=0,
                last_rotated=None,
            ),
            "confluence-api-token": SecretMetadata(
                rotation_count=0,
                last_rotated=None,
            ),
        }

    async def get_secret(
        self,
        secret_name: str,
    ) -> str:

        return self._latest(
            secret_name
        ).value

    async def secret_exists(
        self,
        secret_name: str,
    ) -> bool:
        """
        Check whether secret exists.
        """

        return secret_name in self._secrets

    async def set_secret(
        self,
        secret_name: str,
        secret_value: str,
    ) -> None:

        if secret_name in self._secrets:

            latest = self._latest(
                secret_name
            )

            self._secrets[
                secret_name
            ].append(
                SecretRecord(
                    value=secret_value,
                    version=latest.version + 1,
                )
            )

            self._metadata[
                secret_name
            ].rotation_count += 1

            self._metadata[
                secret_name
            ].last_rotated = (
                datetime.utcnow()
            )

        else:

            self._secrets[
                secret_name
            ] = [
                SecretRecord(
                    value=secret_value,
                    version=1,
                )
            ]

            self._metadata[
                secret_name
            ] = SecretMetadata(
                rotation_count=0,
                last_rotated=None,
            )


    async def get_secret_version(
        self,
        secret_name: str,
    ) -> int:

        return self._latest(
            secret_name
        ).version

    def _latest(
        self,
        secret_name: str,
    ) -> SecretRecord:

        if secret_name not in self._secrets:
            raise KeyError(
                f"Secret not found: {secret_name}"
            )

        return self._secrets[
            secret_name
        ][-1]

    async def get_secret_history(
        self,
        secret_name: str,
    ) -> list[SecretRecord]:
        """
        Return all versions.
        """

        if secret_name not in self._secrets:
            raise KeyError(
                f"Secret not found: {secret_name}"
            )

        return self._secrets[
            secret_name
        ]

    async def rotate_secret(
        self,
        secret_name: str,
        new_secret_value: str,
    ) -> None:
        """
        Simulate secret rotation.
        """

        await self.set_secret(
            secret_name,
            new_secret_value,
        )

    async def get_secret_metadata(
        self,
        secret_name: str,
    ) -> SecretMetadata:
        """
        Return secret metadata.
        """

        if secret_name not in self._metadata:
            raise KeyError(
                f"Secret not found: {secret_name}"
            )

        return self._metadata[
            secret_name
        ]