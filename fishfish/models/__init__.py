from dataclasses import dataclass

from .domain import CreateDomainRequest, Domain, UpdateDomainRequest
from .token import CreateTokenRequest, Token
from .url import URL, CreateURLRequest, UpdateURLRequest


@dataclass
class APIStatus:
    domains: int
    urls: int
    worker: int
    uptime: int
    requests: int
