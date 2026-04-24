from dataclasses import dataclass
from nexsure_api.models import Client


@dataclass
class AddNewClientResponse:
    Client: Client | None = None
