"""One shared async credential so tokens are cached across requests.

Locally, set AZURE_CLI_TENANT_ID to make the Azure CLI login target the tenant that owns
your resources (DefaultAzureCredential does not let you pick a tenant for the CLI).
Leave it unset in Azure so DefaultAzureCredential uses the Function App's managed identity.
"""
import os

from azure.core.credentials_async import AsyncTokenCredential
from azure.identity.aio import AzureCliCredential, DefaultAzureCredential

_credential: AsyncTokenCredential | None = None


def get_credential() -> AsyncTokenCredential:
    global _credential
    if _credential is None:
        cli_tenant = os.getenv("AZURE_CLI_TENANT_ID")
        _credential = (
            AzureCliCredential(tenant_id=cli_tenant) if cli_tenant else DefaultAzureCredential()
        )
    return _credential
