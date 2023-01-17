from dataclasses import dataclass
from typing import Optional

from fishfish.ws.models import WSDomainCreate


@dataclass
class WSDomainUpdate(WSDomainCreate):
    """A websocket domain update event model.

    Attributes
    ----------
    domain: str
        The domain which was deleted.
    description: Optional[str]
        The description for this domain.
    category: Optional[str]
        The category for this domain.
    target: Optional[str]
        The target for this domain.
    checked: Optional[int]
        When this domain was checked into the db?
    """

    checked: Optional[int] = None
