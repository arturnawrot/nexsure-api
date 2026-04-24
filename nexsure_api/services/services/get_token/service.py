from nexsure_api.credentials import Credentials, NoAuth
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.get_token.model import GetTokenResponse


class GetToken(AbstractService[GetTokenResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NoAuth

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/auth/gettoken"

    def get_response_type(self) -> type[GetTokenResponse]:
        return GetTokenResponse

    def get_form_data(self, integration_key: str, integration_login: str, integration_pwd: str, **kwargs) -> dict:
        return {
            "IntegrationKey": integration_key,
            "IntegrationLogin": integration_login,
            "IntegrationPwd": integration_pwd,
        }
