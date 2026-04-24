import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.input_models import AssignmentInput
from nexsure_api.models import Policy
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.add_single_policy.model import AddSinglePolicyResponse
from nexsure_api.types import PolicyMode, PolicyStage, PolicyType


def _xml(tag: str, text: str) -> str:
    return f"<{tag}>{text}</{tag}>"


class AddSinglePolicy(AbstractService[AddSinglePolicyResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/policy/addsinglepolicy"

    def get_response_type(self) -> type[AddSinglePolicyResponse]:
        return AddSinglePolicyResponse

    def get_form_data(
        self,
        client_id: str | int,
        policy_number: str,
        assignment: AssignmentInput,
        eff_date: str,
        exp_date: str,
        description: str = "",
        mode: PolicyMode = PolicyMode.New,
        stage: PolicyStage = PolicyStage.Marketing,
        policy_type: PolicyType = PolicyType.Monoline,
        status: str = "Quote",
        **_,
    ) -> dict:
        assignment_xml = (
            f"<Assignments>"
            f"{_xml('IsPrimary', 'true' if assignment.is_primary else 'false')}"
            f"<Branch>{_xml('BranchID', str(assignment.branch_id))}</Branch>"
            f"<Department>{_xml('DepartmentID', str(assignment.department_id))}</Department>"
            f"</Assignments>"
        )

        policy_xml = (
            '<?xml version="1.0" encoding="utf-8"?>'
            '<Policy xmlns:xsd="http://www.w3.org/2001/XMLSchema" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f"{_xml('PolicyNumber', policy_number)}"
            f"{_xml('PolicyMode', mode)}"
            f"{_xml('PolicyStage', stage)}"
            f"{_xml('PolicyType', policy_type)}"
            f"{_xml('PolicyStatus', status)}"
            f"{_xml('EffDate', eff_date)}"
            f"{_xml('ExpDate', exp_date)}"
            + (f"{_xml('PolicyDescription', description)}" if description else "")
            + "<PolicyDetails/>"
            f"{assignment_xml}"
            "</Policy>"
        )

        return {
            "policyXml": policy_xml,
            "clientId": str(client_id),
            "returnContentType": "application/json",
        }

    def _parse_response(self, response) -> AddSinglePolicyResponse:
        data = response.json()
        policy_data = data.get("Policy", data)
        known = {f.name for f in dataclasses.fields(Policy)}
        policy = Policy(**{k: v for k, v in policy_data.items() if k in known})
        return AddSinglePolicyResponse(Policy=policy)
