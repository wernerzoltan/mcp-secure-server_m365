"""
Secret record model.
"""

from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)
class SecretRecord:
    """
    Represents a stored secret.
    """

    value: str = field(repr=False)
    version: int

@dataclass
class SecretMetadata:
    """
    Metadata for a secret.
    """

    rotation_count: int
    last_rotated: datetime | None