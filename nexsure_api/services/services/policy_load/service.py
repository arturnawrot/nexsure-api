from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.policy_load.model import PolicyLoadResponse


class PolicyLoad(AbstractService[PolicyLoadResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/policy/policyload"

    def get_response_type(self) -> type[PolicyLoadResponse]:
        return PolicyLoadResponse

    def get_query_params(
        self,
        policy_number: str | None = None,
        effective_date: str | None = None,
        expiration_date: str | None = None,
        **kwargs,
    ) -> dict:
        params = {}
        if policy_number is not None:
            params["policyNumber"] = policy_number
        if effective_date is not None:
            params["effectiveDate"] = effective_date
        if expiration_date is not None:
            params["expirationDate"] = expiration_date
        return params
