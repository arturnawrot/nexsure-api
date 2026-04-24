from dataclasses import dataclass, field
from typing import Any


@dataclass
class ClaimDetail:
    ClaimNo: str | None = None
    DateOfLoss: str | None = None
    DateReported: str | None = None
    DateClosed: str | None = None
    Stage: str | None = None
    Status: str | None = None
    EstimatedAmount: str | None = None
    ReservedAmount: str | None = None
    TotalPaidAmount: str | None = None
    Memo: str | None = None
    Reopened: str | None = None


@dataclass
class Claim:
    ClaimID: str | None = None
    PolicyReference: dict[str, Any] | None = None
    ClaimDetail: ClaimDetail | None = None
    Adjustor: dict[str, Any] | None = None
    Claimant: list[dict[str, Any]] = field(default_factory=list)
    ClaimPayment: list[dict[str, Any]] = field(default_factory=list)
    Action: dict[str, Any] | None = None
    CreatedDt: str | None = None
    LastModifiedDt: str | None = None


@dataclass
class ClaimSearchResponse:
    claims: list[Claim] = field(default_factory=list)
    total_pages: int = 0
