import logging

import requests

logger = logging.getLogger(__name__)

DEFAULT_CONNECT_TIMEOUT = 5
DEFAULT_READ_TIMEOUT = 30


class HttpClient:

    def __init__(
        self,
        connect_timeout: int = DEFAULT_CONNECT_TIMEOUT,
        read_timeout: int = DEFAULT_READ_TIMEOUT,
    ) -> None:
        self.timeout = (connect_timeout, read_timeout)
        self.session = requests.Session()

    def request(self, method: str, url: str, **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", self.timeout)

        logger.debug("HTTP %s %s", method, url)

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
        except requests.ConnectionError as exc:
            logger.error("Connection failed for %s %s: %s", method, url, exc)
            raise
        except requests.Timeout as exc:
            logger.error("Request timed out for %s %s: %s", method, url, exc)
            raise
        except requests.HTTPError as exc:
            logger.error(
                "HTTP %s for %s %s: %s",
                response.status_code,
                method,
                url,
                response.text,
            )
            raise requests.HTTPError(
                f"HTTP {response.status_code} for {method} {url}: {response.text}",
                response=response,
            ) from exc

        return response
