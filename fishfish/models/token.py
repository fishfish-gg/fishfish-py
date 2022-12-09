import datetime
from dataclasses import dataclass


@dataclass
class Token:
    """A token from fishfish

    Attributes
    ----------
    token : str
        The token string.
    expires : datetime.datetime
        When the token expires.
    """

    token: str
    expires: datetime.datetime

    @property
    def has_expired(self):
        return self.expires < datetime.datetime.utcnow()
