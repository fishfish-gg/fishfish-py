from __future__ import annotations

from typing import Optional
from dataclasses import dataclass

from fishfish import Category


@dataclass
class URL:
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
