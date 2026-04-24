from dataclasses import dataclass, field
from nexsure_api.models import Policy


@dataclass
class LoadPolicyByPolicyIdResponse:
    Policy: list[Policy] = field(default_factory=list)
