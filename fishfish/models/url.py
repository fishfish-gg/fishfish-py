from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import Optional

from fishfish import Category


@dataclass
class URL:
    """A URL from fishfish

    Attributes
    ----------
    url : str
        The URL string.
    description : str
        The description given by fishfish.
    category : Category
        The category of the URL.
    target : str
        The target of the URL.
    added : int
        When the URL was added.
    checked : int
        The last time the URL was checked.
    """

    url: str
    description: str
    category: Category
    added: datetime.datetime
    checked: datetime.datetime
    target: Optional[str] = None

    @classmethod
    def from_dict(cls, data) -> URL:
        return cls(
            url=data["url"],
            added=datetime.datetime.fromtimestamp(data["added"]),
            checked=datetime.datetime.fromtimestamp(data["checked"]),
            target=data.get("target"),
            description=data["description"],
            category=Category.from_str(data["category"]),
        )
