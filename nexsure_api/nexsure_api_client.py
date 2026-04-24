from nexsure_api.base_api_client import BaseApiClient
from nexsure_api.credentials import Credentials
from nexsure_api.http_client import HttpClient
from nexsure_api.service_factory import ServiceFactory


class ServiceNamespace:

    def __init__(self, api_client: BaseApiClient, services: dict[str, type]) -> None:
        self._api_client = api_client
        self._services = services

    def __getattr__(self, service_name: str):
        try:
            service_class = self._services[service_name]
        except KeyError:
            raise AttributeError(f"Service '{service_name}' not found")
        return service_class(self._api_client)


class NexsureApiClient(BaseApiClient):

    def __init__(self, credentials: list[Credentials], http: HttpClient | None = None) -> None:
        self.service_factory = ServiceFactory()
        super().__init__(credentials, http)
        for group, services in self.service_factory._services.items():
            setattr(self, group, ServiceNamespace(self, services))
