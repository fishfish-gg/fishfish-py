import typing
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
    target: str
    added: int
    checked: int
