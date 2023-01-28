from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class WSDomainDelete:
    """A websocket domain delete event model.

    Attributes
    ----------
    domain: str
        The domain which was deleted.
    """

    domain: str

    @classmethod
    def from_dict(cls, data: dict) -> WSDomainDelete:
        return cls(**data)


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
