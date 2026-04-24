from dataclasses import dataclass, field


@dataclass
class Branch:
    BranchID: int | None = None
    BranchName: str | None = None
    BranchCode: str | None = None
    IsActive: bool | None = None


@dataclass
class SearchBranchByBranchNameResponse:
    Branch: list[Branch] = field(default_factory=list)
