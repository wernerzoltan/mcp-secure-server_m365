from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    Application settings.
    """

    app_name: str = Field(
        default="mcp-secure-server"
    )

    app_env: str = Field(
        default="development"
    )

    log_level: str = Field(
        default="INFO"
    )

    use_real_services: bool = Field(
        default=False
    )

    mcp_server_name: str = Field(
        default="mcp-secure-server"
    )

    class Config:
        env_file = ".env"
        case_sensitive = False