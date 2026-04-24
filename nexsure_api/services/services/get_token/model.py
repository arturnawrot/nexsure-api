from dataclasses import dataclass


@dataclass
class GetTokenResponse:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str | None = None
