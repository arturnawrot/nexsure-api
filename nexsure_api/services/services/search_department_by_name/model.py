from dataclasses import dataclass, field


@dataclass
class Department:
    DepartmentID: str | None = None
    DepartmentName: str | None = None
    DepartmentCode: str | None = None
    IsActive: str | None = None


@dataclass
class SearchDepartmentByNameResponse:
    Department: list[Department] = field(default_factory=list)
