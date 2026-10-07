"""
Why This Exists
Future code can simply use:

    from mcp_server.config import settings
    app_name = settings.app_name

    instead of repeatedly creating:

        from mcp_server.config.settings import Settings
        settings = Settings()

"""


from mcp_server.config.settings import (
    Settings,
)

settings = Settings()

__all__ = [
    "settings",
    "Settings",
]