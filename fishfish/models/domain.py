import typing
from dataclasses import dataclass

from fishfish.enums import Category


@dataclass
class Domain:
    name: str
    description: str
    category: Category
    target: str
    added: int
    checked: int
