from dataclasses import dataclass, field
from typing import Any

from nexsure_api.models import Policy


@dataclass
class PolicySearchWithDetailsResponse:
    policies: list[Policy] = field(default_factory=list)
    total_pages: int = 0
