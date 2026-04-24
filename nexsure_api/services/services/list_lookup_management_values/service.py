import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.models import LookupCategoryType, LookupDefinitionType, LookupDefinitionValueType
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.list_lookup_management_values.model import ListLookupManagementValuesResponse
from nexsure_api.types import LookupCategory


class ListLookupManagementValues(AbstractService[ListLookupManagementValuesResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/lookupdata/listlookupmanagementvalues"

    def get_response_type(self) -> type[ListLookupManagementValuesResponse]:
        return ListLookupManagementValuesResponse

    def get_query_params(self, category_name: LookupCategory, **_) -> dict:
        return {"categoryName": category_name, "returnContentType": "application/json"}

    def _parse_response(self, response) -> ListLookupManagementValuesResponse:
        data = response.json()
        cats_raw = data.get("LookupManagement", data).get("Category", [])
        if isinstance(cats_raw, dict):
            cats_raw = [cats_raw]

        known_cat = {f.name for f in dataclasses.fields(LookupCategoryType)}
        known_type = {f.name for f in dataclasses.fields(LookupDefinitionType)}
        known_item = {f.name for f in dataclasses.fields(LookupDefinitionValueType)}

        categories = []
        for cat_d in cats_raw:
            types_raw = cat_d.get("Type", [])
            if isinstance(types_raw, dict):
                types_raw = [types_raw]
            types = []
            for type_d in types_raw:
                items_raw = type_d.get("DataItem", [])
                if isinstance(items_raw, dict):
                    items_raw = [items_raw]
                items = [LookupDefinitionValueType(**{k: v for k, v in d.items() if k in known_item}) for d in items_raw]
                t = LookupDefinitionType(**{k: v for k, v in type_d.items() if k in known_type and k != "DataItem"})
                t.DataItem = items
                types.append(t)
            cat = LookupCategoryType(**{k: v for k, v in cat_d.items() if k in known_cat and k != "Type"})
            cat.Type = types
            categories.append(cat)

        return ListLookupManagementValuesResponse(Category=categories)
