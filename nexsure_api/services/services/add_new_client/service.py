import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.input_models import AddressInput, AssignmentInput, ContactInput
from nexsure_api.models import Client
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.add_new_client.model import AddNewClientResponse
from nexsure_api.types import ClientStage, ClientType, LegalEntity


def _xml(tag: str, text: str) -> str:
    return f"<{tag}>{text}</{tag}>"


class AddNewClient(AbstractService[AddNewClientResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/clients/addnewclient"

    def get_response_type(self) -> type[AddNewClientResponse]:
        return AddNewClientResponse

    def get_form_data(
        self,
        name: str,
        assignment: AssignmentInput,
        client_type: ClientType = ClientType.Commercial,
        stage: ClientStage = ClientStage.Prospect,
        legal_entity: LegalEntity = LegalEntity.Corporation,
        contacts: list[ContactInput] | None = None,
        addresses: list[AddressInput] | None = None,
        **_,
    ) -> dict:
        names_xml = (
            f"<ClientNames>"
            f"{_xml('Name', name)}"
            f"{_xml('IsPrimaryName', 'true')}"
            f"{_xml('IsDBAName', 'false')}"
            f"{_xml('LegalEntityCd', legal_entity)}"
            f"{_xml('GrossReceipts', '0')}"
            f"</ClientNames>"
        )

        contacts_xml = "".join(
            f"<Contacts>"
            f"{_xml('FirstName', c.first_name)}"
            f"{_xml('LastName', c.last_name)}"
            f"{_xml('IsPrimary', 'true' if c.is_primary else 'false')}"
            f"</Contacts>"
            for c in (contacts or [])
        )

        locations_xml = "".join(
            f"<Locations>"
            f"<Address>"
            f"{_xml('AddressType', addr.address_type)}"
            f"{_xml('StreetAddress1', addr.street)}"
            f"{_xml('City', addr.city)}"
            f"{_xml('State', addr.state)}"
            f"{_xml('ZipCode', addr.zip_code)}"
            f"</Address>"
            f"{_xml('IsPrimaryLocation', 'true')}"
            f"</Locations>"
            for addr in (addresses or [])
        )

        assignment_xml = (
            f"<Assignments>"
            f"{_xml('IsPrimary', 'true' if assignment.is_primary else 'false')}"
            f"<Branch>{_xml('BranchID', str(assignment.branch_id))}</Branch>"
            f"<Department>{_xml('DepartmentID', str(assignment.department_id))}</Department>"
            f"</Assignments>"
        )

        client_xml = (
            '<?xml version="1.0" ?>'
            '<Client xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
            'xmlns:xsd="http://www.w3.org/2001/XMLSchema">'
            f"{_xml('ClientType', client_type)}"
            f"{_xml('ClientStage', stage)}"
            f"{names_xml}{contacts_xml}{locations_xml}{assignment_xml}"
            "</Client>"
        )

        return {"inputXml": client_xml, "returnContentType": "application/json"}

    def _parse_response(self, response) -> AddNewClientResponse:
        data = response.json()
        client_data = data.get("Client", data)
        known = {f.name for f in dataclasses.fields(Client)}
        client = Client(**{k: v for k, v in client_data.items() if k in known})
        return AddNewClientResponse(Client=client)
