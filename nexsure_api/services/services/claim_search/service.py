import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.claim_search.model import Claim, ClaimDetail, ClaimSearchResponse
from nexsure_api.types import SearchType


class ClaimSearch(AbstractService[ClaimSearchResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/claims/claimsearch"

    def get_response_type(self) -> type[ClaimSearchResponse]:
        return ClaimSearchResponse

    def get_query_params(self, page: int = 1, results_per_page: int = 20, **_) -> dict:
        return {
            "page": page,
            "resultsPerPage": results_per_page,
            "returnContentType": "application/json",
        }

    def get_body(
        self,
        client_id: int = 0,
        client_name: str = "",
        claim_number: str = "",
        policy_number: str = "",
        claimant_name: str = "",
        adjustor_name: str = "",
        date_of_loss_from: str = "",
        date_of_loss_to: str = "",
        search_type: SearchType = SearchType.Contains,
        **_,
    ) -> dict:
        body: dict = {"SearchType": int(search_type)}
        if client_id:
            body["ClientID"] = client_id
        if client_name:
            body["ClientName"] = client_name
        if claim_number:
            body["ClaimNumber"] = claim_number
        if policy_number:
            body["PolicyNumber"] = policy_number
        if claimant_name:
            body["ClaimantName"] = claimant_name
        if adjustor_name:
            body["AdjustorName"] = adjustor_name
        if date_of_loss_from:
            body["DateOfLossFrom"] = date_of_loss_from
        if date_of_loss_to:
            body["DateOfLossTo"] = date_of_loss_to
        return body

    def _parse_response(self, response) -> ClaimSearchResponse:
        data = response.json().get("Claims", {})
        raw = data.get("Claim", [])
        if isinstance(raw, dict):
            raw = [raw]

        known_claim = {f.name for f in dataclasses.fields(Claim)}
        known_detail = {f.name for f in dataclasses.fields(ClaimDetail)}

        claims = []
        for c in raw:
            detail_raw = c.get("ClaimDetail")
            detail = (
                ClaimDetail(**{k: v for k, v in detail_raw.items() if k in known_detail})
                if isinstance(detail_raw, dict) else None
            )
            claim = Claim(**{k: v for k, v in c.items() if k in known_claim and k != "ClaimDetail"})
            claim.ClaimDetail = detail
            claims.append(claim)

        return ClaimSearchResponse(
            claims=claims,
            total_pages=int(data.get("TotalPages", 0)),
        )
