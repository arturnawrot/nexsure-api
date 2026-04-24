from dataclasses import dataclass
from nexsure_api.models import Attachment


@dataclass
class AddAttachmentResponse:
    Attachment: Attachment | None = None
