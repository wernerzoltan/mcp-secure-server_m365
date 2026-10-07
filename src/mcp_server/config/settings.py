from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    Application settings.
    """

    #
    # Application
    #

    app_name: str = Field(
        default="mcp-secure-server"
    )

    app_env: str = Field(
        default="development"
    )

    #
    # Logging
    #

    log_level: str = Field(
        default="INFO"
    )

    #
    # Service Mode
    #

    use_real_services: bool = Field(
        default=False
    )

    #
    # MCP Server
    #

    mcp_server_name: str = Field(
        default="mcp-secure-server"
    )

    #
    # Okta
    #

    okta_issuer: str = Field(
        default="https://mock-okta.local"
    )

    okta_client_id: str = Field(
        default="mock-client-id"
    )

    okta_client_secret: str = Field(
        default="mock-client-secret"
    )

    #
    # Azure Key Vault
    #

    azure_key_vault_url: str = Field(
        default="https://mock-keyvault.local"
    )

    #
    # Confluence
    #

    confluence_base_url: str = Field(
        default="https://mock-confluence.local"
    )

    class Config:
        env_file = ".env"
        case_sensitive = False