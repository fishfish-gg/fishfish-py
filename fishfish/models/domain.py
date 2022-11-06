from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from fishfish.enums import Category


@dataclass
class Domain:
    name: str
    description: str
    category: Category
    added: int
    checked: int
    target: Optional[str]

    @classmethod
    def from_dict(cls, data) -> Domain:
        return cls(
            name=data["name"],
            added=data["added"],
            checked=data["checked"],
            target=data.get("target"),
            description=data["description"],
            category=Category.from_str(data["category"]),
        )
