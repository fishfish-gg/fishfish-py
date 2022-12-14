from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import Optional

from fishfish.enums import Category


@dataclass
class Domain:
    """A domain from fishfish

    Attributes
    ----------
    name : str
        The domains name.
    description : str
        The domains description
    category : Category
        Whether a domain is safe|phishing|malware
    target : str
        The target of the domain
    added : int
        When the domain was added.
    checked : int
        The last time the domain was checked
    """

    name: str
    description: str
    category: Category
    added: datetime.datetime
    checked: datetime.datetime
    target: Optional[str]

    @classmethod
    def from_dict(cls, data) -> Domain:
        return cls(
            name=data["name"],
            added=datetime.datetime.fromtimestamp(data["added"]),
            checked=datetime.datetime.fromtimestamp(data["checked"]),
            target=data.get("target"),
            description=data["description"],
            category=Category.from_str(data["category"]),
        )
