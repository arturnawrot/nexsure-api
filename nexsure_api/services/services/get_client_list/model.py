from dataclasses import dataclass, field


@dataclass
class ClientListItem:
    ClientId: str | None = None
    ClientName: str | None = None
    ClientType: str | None = None
    ClientStage: str | None = None
    ClientLocationName: str | None = None
    LocAddress1: str | None = None
    LocAddress2: str | None = None
    LocCity: str | None = None
    LocState: str | None = None
    LocZipCode: str | None = None


@dataclass
class GetClientListResponse:
    clients: list[ClientListItem] = field(default_factory=list)
