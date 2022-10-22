from dataclasses import dataclass
import typing
from fishfish.enums import Category


@dataclass
class Domain:
    name: str
    description: str
    category: Category
    target: str
    added: int
    checked: int


@dataclass
class CreateDomainRequest:
    description: str
    category: Category
    target: typing.Optional[str]


@dataclass
class UpdateDomainRequest:
    description: typing.Optional[str]
    category: typing.Optional[Category]
    target: typing.Optional[str]



