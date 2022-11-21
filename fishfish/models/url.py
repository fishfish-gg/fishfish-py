from __future__ import annotations

from typing import Optional
from dataclasses import dataclass

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
    added: int
    checked: int
    target: Optional[str]

    @classmethod
    def from_dict(cls, data) -> URL:
        return cls(
            url=data["url"],
            added=data["added"],
            checked=data["checked"],
            target=data.get("target"),
            description=data["description"],
            category=Category.from_str(data["category"]),
        )
