from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.client_search.model import ClientSearchResponse


class ClientSearch(AbstractService[ClientSearchResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/clients/clientsearch"

    def get_response_type(self) -> type[ClientSearchResponse]:
        return ClientSearchResponse

    def get_body(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        company_name: str | None = None,
        client_code: str | None = None,
        **kwargs,
    ) -> dict:
        body = {}
        if first_name is not None:
            body["FirstName"] = first_name
        if last_name is not None:
            body["LastName"] = last_name
        if company_name is not None:
            body["CompanyName"] = company_name
        if client_code is not None:
            body["ClientCode"] = client_code
        return body
