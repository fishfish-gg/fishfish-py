from dataclasses import dataclass
from typing import Optional

from fishfish.ws.models import WSUrlDelete


@dataclass
class WSUrlCreate(WSUrlDelete):
    """A websocket url create event model.

    Attributes
    ----------
    url: str
        The url which was deleted.
    description: Optional[str]
        The description for this url.
    category: Optional[str]
        The category for this url.
    target: Optional[str]
        The target for this url.
    """

    description: Optional[str] = None
    category: Optional[str] = None
    target: Optional[str] = None
