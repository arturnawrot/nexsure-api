from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.update_client.model import UpdateClientResponse


class UpdateClient(AbstractService[UpdateClientResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/clients/updateclient"

    def get_response_type(self) -> type[UpdateClientResponse]:
        return UpdateClientResponse

    def get_form_data(self, client_xml: str, **kwargs) -> dict:
        return {"inputXml": client_xml}
