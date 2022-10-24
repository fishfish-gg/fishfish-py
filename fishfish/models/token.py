import typing
from dataclasses import dataclass, field


@dataclass
class Token:
    token: str
    expires: int
