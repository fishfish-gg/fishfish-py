from dataclasses import dataclass
from typing import Optional

from fishfish.ws.models import WSDomainDelete


@dataclass
class WSDomainCreate(WSDomainDelete):
    """A websocket domain create event model.

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
    """

    description: Optional[str] = None
    category: Optional[str] = None
    target: Optional[str] = None
