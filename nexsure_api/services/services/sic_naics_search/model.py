from dataclasses import dataclass, field


@dataclass
class NaicSicCode:
    CodeID: str | None = None
    NaicsCode: str | None = None
    NaicsDescription: str | None = None
    SicCode: str | None = None
    SicDescription: str | None = None


@dataclass
class SicNaicsSearchResponse:
    codes: list[NaicSicCode] = field(default_factory=list)
    total_pages: int = 0
