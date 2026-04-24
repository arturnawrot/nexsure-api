import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.sic_naics_search.model import NaicSicCode, SicNaicsSearchResponse
from nexsure_api.types import SearchType


class SicNaicsSearch(AbstractService[SicNaicsSearchResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/lookupdata/sicnaicssearch"

    def get_response_type(self) -> type[SicNaicsSearchResponse]:
        return SicNaicsSearchResponse

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
        naics_description: str = "",
        sic_description: str = "",
        naics_code: str = "",
        sic_code: str = "",
        search_type: SearchType = SearchType.Contains,
        **_,
    ) -> dict:
        return {
            "SearchType": int(search_type),
            "NaicsCode": naics_code,
            "NaicsDescription": naics_description,
            "SicCode": sic_code,
            "SicDescription": sic_description,
            "SortField1": 0,
            "SortType1": 0,
        }

    def _parse_response(self, response) -> SicNaicsSearchResponse:
        data = response.json().get("SicNaicsList", {})
        raw = data.get("NaicSicCode", [])
        if isinstance(raw, dict):
            raw = [raw]
        known = {f.name for f in dataclasses.fields(NaicSicCode)}
        codes = [NaicSicCode(**{k: v for k, v in c.items() if k in known}) for c in raw]
        return SicNaicsSearchResponse(
            codes=codes,
            total_pages=int(data.get("TotalPages", 0)),
        )
