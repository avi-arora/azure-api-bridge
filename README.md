# VeritlexAI Azure API Bridge

FastAPI app hosted on Azure Functions (Python v2 model, ASGI adapter).

## Endpoints

| Method | Path                | Description |
|--------|---------------------|-------------|
| GET    | `/agents`           | Lists model deployments from the Azure AI Foundry project. |
| GET    | `/veritlexai/token` | Returns an Entra ID token for Cognitive Services plus the mobile model endpoint and API version. |
| GET    | `/health`           | Liveness check. |

No auth and no caching for now. `routePrefix` is `""` in `host.json`, so the paths have no `/api` prefix.

## Layout

```
function_app.py          # Azure Functions entry point (AsgiFunctionApp)
app/main.py              # FastAPI app
app/config.py            # env-based settings
app/routers/             # agents.py, token.py
app/services/            # foundry.py, tokens.py, credentials.py
```

## Run locally

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp local.settings.example.json local.settings.json   # fill in values
az login                                              # DefaultAzureCredential uses your CLI login
func start
```

Or run FastAPI directly (export the env vars first): `uvicorn app.main:app --reload`.

## Configuration

| Setting | Purpose |
|---------|---------|
| `AZURE_CLI_TENANT_ID` | Local only. Tenant to use with your `az login` session when the resources aren't in your default tenant. Leave unset in Azure (managed identity is used). |
| `AZURE_AI_PROJECT_ENDPOINT` | Azure AI Foundry project endpoint |
| `MOBILE_MODEL_DEPLOYMENT_URL`, `MODEL_API_VERSION` | Returned by `/veritlexai/token` |

## Deploy

```bash
func azure functionapp publish <function-app-name>
```

Give the Function App's managed identity these roles:
- **Azure AI User** (or Contributor) on the AI Foundry project, to list deployments
- **Cognitive Services User** on the Azure OpenAI resource, to get tokens
# azure-api-bridge
