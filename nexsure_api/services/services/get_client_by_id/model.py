from dataclasses import dataclass, field
from nexsure_api.models import Client


@dataclass
class GetClientByIdResponse:
    Client: list[Client] = field(default_factory=list)
