from dataclasses import dataclass
from typing import Optional

from fishfish.ws.models import WSUrlCreate


@dataclass
class WSUrlUpdate(WSUrlCreate):
    """A websocket url update event model.

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
    checked: Optional[int]
        When this url was checked into the db?
    """

    checked: Optional[int] = None
