from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.get_client_by_id.model import GetClientByIdResponse


class GetClientById(AbstractService[GetClientByIdResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/clients/getclientbyid"

    def get_response_type(self) -> type[GetClientByIdResponse]:
        return GetClientByIdResponse

    def get_query_params(self, client_id: int, **kwargs) -> dict:
        return {"clientId": client_id}
