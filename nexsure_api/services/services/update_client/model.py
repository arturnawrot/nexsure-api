from dataclasses import dataclass
from nexsure_api.models import Client


@dataclass
class UpdateClientResponse:
    Client: Client | None = None
