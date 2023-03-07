from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class WSUrlDelete:
    """A websocket url delete event model.

    Attributes
    ----------
    url: str
        The url which was deleted.
    """

    url: str

    @classmethod
    def from_dict(cls, data: dict) -> WSUrlDelete:
        return cls(**data)


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
