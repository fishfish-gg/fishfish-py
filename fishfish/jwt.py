from datetime import datetime
from typing import Union


class JWT:
    def __init__(self, token: str, expires_at: Union[int, float]):
        self.token: str = token
        self.expires_at: datetime = datetime.fromtimestamp(expires_at)

    @property
    def has_expired(self) -> bool:
        return self.expires_at < datetime.utcnow()
