from dataclasses import dataclass, field
from nexsure_api.models import LookupCategoryType


@dataclass
class ListLookupManagementValuesResponse:
    Category: list[LookupCategoryType] = field(default_factory=list)
