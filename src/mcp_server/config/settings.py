from pydantic_settings import BaseSettings
from pydantic import Field
from pydantic import computed_field


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

    #
    # Environment Helpers
    #

    @computed_field
    @property
    def is_development(self) -> bool:
        """
        True when running in development.
        """

        return self.app_env.lower() == "development"

    @computed_field
    @property
    def is_production(self) -> bool:
        """
        True when running in production.
        """

        return self.app_env.lower() == "production"

    @computed_field
    @property
    def using_mock_services(self) -> bool:
        """
        True when mock implementations
        should be used.
        """

        return not self.use_real_services

    @computed_field
    @property
    def using_real_services(self) -> bool:
        """
        True when real implementations
        should be used.
        """

        return self.use_real_services

    class Config:
        env_file = ".env"
        case_sensitive = False