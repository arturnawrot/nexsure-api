from dataclasses import dataclass, field
from nexsure_api.models import Attachment


@dataclass
class GetAttachmentListResponse:
    Attachment: list[Attachment] = field(default_factory=list)
