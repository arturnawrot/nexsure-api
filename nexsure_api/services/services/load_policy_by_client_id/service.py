from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.load_policy_by_client_id.model import LoadPolicyByClientIdResponse


class LoadPolicyByClientId(AbstractService[LoadPolicyByClientIdResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/policy/loadpolicybyclientid"

    def get_response_type(self) -> type[LoadPolicyByClientIdResponse]:
        return LoadPolicyByClientIdResponse

    def get_query_params(self, client_id: int, **kwargs) -> dict:
        return {"clientId": client_id}
