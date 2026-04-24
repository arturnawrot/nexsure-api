import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.models import Policy
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.policy_search_with_details.model import PolicySearchWithDetailsResponse
from nexsure_api.types import SearchType


class PolicySearchWithDetails(AbstractService[PolicySearchWithDetailsResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/policy/policysearchwithdetails"

    def get_response_type(self) -> type[PolicySearchWithDetailsResponse]:
        return PolicySearchWithDetailsResponse

    def get_query_params(
        self,
        page: int = 1,
        results_per_page: int = 20,
        **_,
    ) -> dict:
        return {
            "page": page,
            "resultsPerPage": results_per_page,
            "returnContentType": "application/json",
        }

    def get_body(
        self,
        client_name: str = "",
        client_id: int = 0,
        policy_number: str = "",
        include_history: bool = False,
        search_type: SearchType = SearchType.Contains,
        **_,
    ) -> dict:
        return {
            "SearchType": int(search_type),
            "ClientID": client_id,
            "ClientName": client_name,
            "PolicyMode": 0,
            "PolicyStage": 0,
            "PolicyStatus": 0,
            "PolicyType": 0,
            "IncludeHistory": include_history,
            "PolicyNumber": policy_number,
        }

    def _parse_response(self, response) -> PolicySearchWithDetailsResponse:
        data = response.json()
        policies_data = data.get("Policies", data)
        raw = policies_data.get("Policy", [])
        if isinstance(raw, dict):
            raw = [raw]
        known = {f.name for f in dataclasses.fields(Policy)}
        policies = [Policy(**{k: v for k, v in p.items() if k in known}) for p in raw]
        total_pages = int(policies_data.get("TotalPages", 0))
        return PolicySearchWithDetailsResponse(policies=policies, total_pages=total_pages)
