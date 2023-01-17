from __future__ import annotations

from dataclasses import dataclass


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
