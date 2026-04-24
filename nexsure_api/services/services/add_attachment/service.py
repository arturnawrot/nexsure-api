import base64
import dataclasses

from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.models import Attachment
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.add_attachment.model import AddAttachmentResponse


class AddAttachment(AbstractService[AddAttachmentResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/attachments/addattachment"

    def get_response_type(self) -> type[AddAttachmentResponse]:
        return AddAttachmentResponse

    def get_query_params(
        self,
        client_id: int | None = None,
        policy_id: int | None = None,
        file_name: str = "attachment.pdf",
        description: str = "",
        file_bytes: bytes | None = None,
        **_,
    ) -> dict:
        assignment_type = "Policy" if policy_id is not None else "Client"
        assignment_id = policy_id if policy_id is not None else client_id

        attachment_xml = (
            '<?xml version="1.0" encoding="utf-8"?>'
            '<Attachment xmlns:xsd="http://www.w3.org/2001/XMLSchema" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f'<AssignedTo><AssignmentType>{assignment_type}</AssignmentType>'
            f'<AssignmentTypeID>{assignment_id}</AssignmentTypeID></AssignedTo>'
            f'<AttachmentName>{description or file_name}</AttachmentName>'
            f'<AttachmentDesc>{description}</AttachmentDesc>'
            f'<FileName>{file_name}</FileName>'
            '</Attachment>'
        )

        content = file_bytes if file_bytes is not None else b"placeholder"
        attachment_b64 = base64.b64encode(content).decode()

        return {
            "xml": attachment_xml,
            "attachmentBase64": attachment_b64,
            "returnContentType": "application/json",
        }

    def _parse_response(self, response) -> AddAttachmentResponse:
        data = response.json()
        attachment_data = data.get("Attachment", data)
        known = {f.name for f in dataclasses.fields(Attachment)}
        attachment = Attachment(**{k: v for k, v in attachment_data.items() if k in known})
        return AddAttachmentResponse(Attachment=attachment)
