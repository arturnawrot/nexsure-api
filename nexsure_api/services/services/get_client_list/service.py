import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.get_client_list.model import ClientListItem, GetClientListResponse


class GetClientList(AbstractService[GetClientListResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/clients/getclientlist"

    def get_response_type(self) -> type[GetClientListResponse]:
        return GetClientListResponse

    def get_form_data(self, client_name: str, **_) -> dict:
        return {"clientName": client_name, "returnContentType": "application/json"}

    def _parse_response(self, response) -> GetClientListResponse:
        raw = response.json().get("Clients", {}).get("Client", [])
        if isinstance(raw, dict):
            raw = [raw]
        known = {f.name for f in dataclasses.fields(ClientListItem)}
        clients = [ClientListItem(**{k: v for k, v in c.items() if k in known}) for c in raw]
        return GetClientListResponse(clients=clients)
