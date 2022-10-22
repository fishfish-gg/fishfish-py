from dataclasses import dataclass
from fishfish import Category
import typing


@dataclass
class URL:
    url: str
    description: str
    category: Category
    target: str
    added: int
    checked: int


@dataclass
class CreateURLRequest:
    description: str
    category: Category
    target: typing.Optional[str]


@dataclass
class UpdateURLRequest:
    description: str
    category: Category
    target: typing.Optional[str]
