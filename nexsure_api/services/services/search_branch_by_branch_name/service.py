import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.search_branch_by_branch_name.model import Branch, SearchBranchByBranchNameResponse


class SearchBranchByBranchName(AbstractService[SearchBranchByBranchNameResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/organization/searchbranchbybranchname"

    def get_response_type(self) -> type[SearchBranchByBranchNameResponse]:
        return SearchBranchByBranchNameResponse

    def get_form_data(self, branch_name: str = "", **kwargs) -> dict:
        data = {"returnContentType": "application/json"}
        if branch_name:
            data["branchName"] = branch_name
        return data

    def _parse_response(self, response) -> SearchBranchByBranchNameResponse:
        raw = response.json().get("Branches", {}).get("Branch", [])
        known = {f.name for f in dataclasses.fields(Branch)}
        branches = [Branch(**{k: v for k, v in b.items() if k in known}) for b in raw]
        return SearchBranchByBranchNameResponse(Branch=branches)
