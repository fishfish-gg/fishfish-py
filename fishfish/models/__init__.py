from dataclasses import dataclass
from .domain import Domain, CreateDomainRequest, UpdateDomainRequest
from .token import Token, CreateTokenRequest
from .url import URL, CreateURLRequest, UpdateURLRequest


@dataclass
class APIStatus:
    domains: int
    urls: int
    worker: int
    uptime: int
    requests: int
