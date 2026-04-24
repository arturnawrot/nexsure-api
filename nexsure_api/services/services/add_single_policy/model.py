from dataclasses import dataclass
from nexsure_api.models import Policy


@dataclass
class AddSinglePolicyResponse:
    Policy: Policy | None = None
