import typing
from dataclasses import dataclass

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
    target: str
    added: int
    checked: int
