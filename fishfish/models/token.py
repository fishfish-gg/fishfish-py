import typing
from dataclasses import dataclass, field


@dataclass
class Token:
    token: str
    expires: int


@dataclass
class CreateTokenRequest:
    permissions: typing.List[str] = field(default_factory=lambda: [])
