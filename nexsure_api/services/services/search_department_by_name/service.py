import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.search_department_by_name.model import Department, SearchDepartmentByNameResponse


class SearchDepartmentByName(AbstractService[SearchDepartmentByNameResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/organization/searchdepartmentbyname"

    def get_response_type(self) -> type[SearchDepartmentByNameResponse]:
        return SearchDepartmentByNameResponse

    def get_form_data(self, department_name: str = "%%", **kwargs) -> dict:
        return {"departmentName": department_name, "returnContentType": "application/json"}

    def _parse_response(self, response) -> SearchDepartmentByNameResponse:
        raw = response.json().get("Departments", {}).get("Department", [])
        if isinstance(raw, dict):
            raw = [raw]
        known = {f.name for f in dataclasses.fields(Department)}
        departments = [Department(**{k: v for k, v in d.items() if k in known}) for d in raw]
        return SearchDepartmentByNameResponse(Department=departments)
