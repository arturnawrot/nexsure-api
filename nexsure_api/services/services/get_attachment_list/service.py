from nexsure_api.credentials import Credentials, NexsureCredentials
from nexsure_api.enums import HttpMethod
from nexsure_api.services.abstract_service import AbstractService
from nexsure_api.services.services.get_attachment_list.model import GetAttachmentListResponse


class GetAttachmentList(AbstractService[GetAttachmentListResponse]):

    def get_credentials_class(self) -> type[Credentials]:
        return NexsureCredentials

    def get_method(self) -> HttpMethod:
        return HttpMethod.POST

    def get_url_path(self) -> str:
        return "/attachments/getattachmentlist"

    def get_response_type(self) -> type[GetAttachmentListResponse]:
        return GetAttachmentListResponse

    def get_query_params(
        self,
        client_id: int | None = None,
        policy_id: int | None = None,
        **kwargs,
    ) -> dict:
        params = {}
        if client_id is not None:
            params["clientId"] = client_id
        if policy_id is not None:
            params["policyId"] = policy_id
        return params
