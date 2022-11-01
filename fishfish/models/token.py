import typing
from dataclasses import dataclass, field


@dataclass
class Token:
    """A token from fishfish
    
    Attributes
    ----------
    token : str
        The token string.
    expires : int
        When the token expires.
    """
    token: str
    expires: int
