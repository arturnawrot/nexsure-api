from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.get_client_by_name.model import GetClientByNameResponse


class GetClientByName(AbstractService[GetClientByNameResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/clients/getclientbyname"

    def get_response_type(self) -> type[GetClientByNameResponse]:
        return GetClientByNameResponse

    def get_query_params(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        company_name: str | None = None,
        **kwargs,
    ) -> dict:
        params = {}
        if first_name is not None:
            params["firstName"] = first_name
        if last_name is not None:
            params["lastName"] = last_name
        if company_name is not None:
            params["companyName"] = company_name
        return params
