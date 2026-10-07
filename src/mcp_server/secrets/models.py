"""
Secret record model.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class SecretRecord:
    """
    Represents a stored secret.
    """

    value: str
    version: int

@dataclass
class SecretMetadata:
    """
    Metadata for a secret.
    """

    rotation_count: int
    last_rotated: datetime | None