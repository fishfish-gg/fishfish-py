from __future__ import annotations

from enum import Enum


class Category(Enum):
    """The category a domain or URL has.

    Attributes
    ----------
    SAFE : str
        The category|domain is safe.
    PHISHING : str
        The category|domain is phishing.
    MALWARE : str
        The category|domain is malware.
    """
    SAFE = "safe"
    PHISHING = "phishing"
    MALWARE = "malware"

    @classmethod
    def from_str(cls, string: str) -> Category:
        return getattr(cls, string.upper())


class Permission(Enum):
    """The permissions a token has.

    Attributes
    ----------
    DOMAINS : str
        The permission to POST/PATCH/DELETE domains.
    URLS : str
        The permission to POST/PATCH/DELETE urls.
    """
    DOMAINS = "domains"
    URLS = "urls"
