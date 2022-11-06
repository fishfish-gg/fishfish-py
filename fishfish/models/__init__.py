from dataclasses import dataclass

from .domain import Domain
from .token import Token
from .url import URL


@dataclass
class APIStatus:
    domains: int
    urls: int
    worker: int
    uptime: int
    requests: int
