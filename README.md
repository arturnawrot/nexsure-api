# nexsure-api

A Python client library for the [Nexsure](https://nexsure.com) EAI (Enterprise Application Integration) API. Built around a clean, extensible service pattern - adding new endpoints takes minutes.

> **Note:** This library is a work in progress. Not all Nexsure API endpoints are implemented yet. See [Available Services](#available-services) for what's ready, and [Adding a New Service](#adding-a-new-service) for how to contribute the rest - the pattern is straightforward and consistent.

---

## Installation

```bash
git clone https://github.com/arturnawrot/nexsure-api
pip install -r requirements.txt
```

Requires Python 3.14+.

---

## Quick Start

```python
from nexsure_api.nexsure_api_client import NexsureApiClient
from nexsure_api.credentials import NoAuth, NexsureCredentials

client = NexsureApiClient(credentials=[NoAuth()])

token = client.services.GetToken.execute(
    integration_key="your-key",
    integration_login="your-login",
    integration_pwd="your-password",
)

client.add_credentials(NexsureCredentials(api_token=token.access_token))

clients = client.services.GetClientList.execute(client_name="acme")
```

---

## Authentication

Nexsure uses a bearer token. Call `GetToken` first - it requires no prior credentials - then add the result to your client.

```python
from nexsure_api.nexsure_api_client import NexsureApiClient
from nexsure_api.credentials import NoAuth, NexsureCredentials

client = NexsureApiClient(credentials=[NoAuth()])

token = client.services.GetToken.execute(
    integration_key="your-key",
    integration_login="your-login",
    integration_pwd="your-password",
)

client.add_credentials(NexsureCredentials(api_token=token.access_token))

# All authenticated services are now available
policy = client.services.LoadPolicyByPolicyId.execute(policy_id=12345)
```

---

## Available Services

Services live under `nexsure_api/services/services/` and are auto-discovered at runtime - no registration needed.

### Client Services

| Service | Method | Endpoint | Description |
|---|---|---|---|
| `GetToken` | POST | `/auth/gettoken` | Authenticate and get bearer token |
| `GetClientList` | POST | `/clients/getclientlist` | List clients by name |
| `GetClientById` | POST | `/clients/getclientbyid` | Get client details by ID |
| `GetClientByName` | POST | `/clients/getclientbyname` | Get client by first/last/company name |
| `ClientSearch` | POST | `/clients/clientsearch` | Search clients by multiple criteria |
| `AddNewClient` | POST | `/clients/addnewclient` | Create a new client |
| `UpdateClient` | POST | `/clients/updateclient` | Update an existing client |

### Policy Services

| Service | Method | Endpoint | Description |
|---|---|---|---|
| `AddSinglePolicy` | POST | `/policy/addsinglepolicy` | Add a policy to a client |
| `LoadPolicyByClientId` | POST | `/policy/loadpolicybyclientid` | Get all policies for a client |
| `LoadPolicyByPolicyId` | POST | `/policy/loadpolicybypolicyid` | Get a policy by ID |
| `PolicyLoad` | POST | `/policy/policyload` | Load a policy by number and date range |
| `PolicySearchWithDetails` | POST | `/policy/policysearchwithdetails` | Search policies with full details |

### Claims Services

| Service | Method | Endpoint | Description |
|---|---|---|---|
| `ClaimSearch` | POST | `/claims/claimsearch` | Search claims by multiple criteria |

### Attachment Services

| Service | Method | Endpoint | Description |
|---|---|---|---|
| `AddAttachment` | POST | `/attachments/addattachment` | Upload a file attachment |
| `GetAttachmentList` | POST | `/attachments/getattachmentlist` | List attachments for a client or policy |

### Organization Services

| Service | Method | Endpoint | Description |
|---|---|---|---|
| `SearchBranchByBranchName` | POST | `/organization/searchbranchbybranchname` | Search branches by name |
| `SearchDepartmentByName` | POST | `/organization/searchdepartmentbyname` | Search departments by name |

### Lookup Services

| Service | Method | Endpoint | Description |
|---|---|---|---|
| `SicNaicsSearch` | POST | `/lookupdata/sicnaicssearch` | Search industry classification codes |
| `ListLookupManagementValues` | POST | `/lookupdata/listlookupmanagementvalues` | Get lookup data categories |

---

## Usage Examples

### Search Clients

```python
results = client.services.ClientSearch.execute(
    client_name="acme",
    client_type="Commercial",
)

for c in results:
    print(c.client_id, c.company_name, c.city)
```

### Load Policies for a Client

```python
policies = client.services.LoadPolicyByClientId.execute(client_id=10042)

for p in policies:
    print(p.policy_number, p.line_of_business, p.effective_date, p.expiration_date)
```

### Search Claims

```python
claims = client.services.ClaimSearch.execute(
    client_id=10042,
    claim_status="Open",
)

for claim in claims:
    print(claim.claim_number, claim.loss_date, claim.status)
```

### Upload an Attachment

```python
with open("certificate.pdf", "rb") as f:
    content = f.read()

client.services.AddAttachment.execute(
    client_id=10042,
    file_name="certificate.pdf",
    file_content=content,
)
```

### Search SIC/NAICS Codes

```python
codes = client.services.SicNaicsSearch.execute(description="restaurant")

for code in codes:
    print(code.code, code.description)
```

---

## Demo

A Jupyter notebook at [demo.ipynb](demo.ipynb) walks through the full flow end-to-end:

1. Acquire a bearer token
2. Discover branches and departments
3. Create a new client
4. Add a policy
5. Upload an attachment
6. Read lookup data
7. Search clients, policies, and claims

Run it with:

```bash
jupyter notebook demo.ipynb
```

---

## Adding a New Service

Every service follows the same pattern. Here's how to add a new one in a few minutes.

### 1. Create the folder structure

```
nexsure_api/services/services/my_endpoint/
    __init__.py
    model.py
    service.py
```

### 2. Define the response model (`model.py`)

```python
from dataclasses import dataclass

@dataclass
class MyEndpointResponse:
    id: int | None = None
    name: str | None = None
    status: str | None = None
```

### 3. Implement the service (`service.py`)

The four abstract methods are required. The optional ones - `get_query_params`, `get_body`, `get_form_data`, and `get_headers` - only need to be overridden if the endpoint uses them.

```python
from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from .model import MyEndpointResponse


class MyEndpoint(AbstractService[MyEndpointResponse]):

    # --- Required ---

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials     # or NoAuth

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST        # GET, POST, PUT, PATCH, DELETE

    def get_url_path(self) -> str:
        return "/my/endpoint"

    def get_response_type(self) -> type[MyEndpointResponse]:
        return MyEndpointResponse

    # --- Optional overrides ---

    def get_query_params(self, item_id: int, **kwargs) -> dict | None:
        return {"id": item_id}

    def get_body(self, name: str, active: bool, **kwargs) -> dict | None:
        return {"name": name, "active": active}

    def get_form_data(self, **kwargs) -> dict | None:
        return {"formKey": "formValue"}

    def get_headers(self, **kwargs) -> dict:
        return {"Accept": "application/json"}
```

### 4. Export from `__init__.py`

```python
from nexsure_api.services.services.my_endpoint.service import MyEndpoint
from nexsure_api.services.services.my_endpoint.model import MyEndpointResponse

__all__ = ["MyEndpoint", "MyEndpointResponse"]
```

That's it. The `ServiceFactory` auto-discovers all concrete `AbstractService` subclasses at startup - your new service will be immediately available as `client.services.MyEndpoint`.

### How the service layer works

When you call `client.services.MyEndpoint.execute(item_id=42)`, the following happens:

1. **Credentials lookup** - finds the first credential of the type returned by `get_credentials_class()` in the client's credential list. Raises `LookupError` if none match.
2. **URL construction** - combines the base URL and `get_url_path()` into a final URL.
3. **Query parameters** - built from `get_query_params(**kwargs)` and appended to the URL.
4. **Headers** - merges the credential's auth header with anything returned by `get_headers(**kwargs)`. Service headers take precedence on conflict.
5. **Body / form data** - merges the credential's body (if any) with `get_body(**kwargs)` or `get_form_data(**kwargs)`. Service values take precedence on conflict.
6. **HTTP request** - delegates to `HttpClient.request()` which uses a `requests.Session` with a 5s connect / 30s read timeout and calls `raise_for_status()`.
7. **Deserialization** - calls `response.json()` and unpacks it into the dataclass returned by `get_response_type()`.

---

## License

MIT
