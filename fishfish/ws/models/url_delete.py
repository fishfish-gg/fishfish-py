from __future__ import annotations

from dataclasses import dataclass


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
