import typing
from dataclasses import dataclass

from fishfish import Category


@dataclass
class URL:
    url: str
    description: str
    category: Category
    target: str
    added: int
    checked: int
