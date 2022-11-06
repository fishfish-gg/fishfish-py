from __future__ import annotations

from enum import Enum


class Category(Enum):
    SAFE = "safe"
    PHISHING = "phishing"
    MALWARE = "malware"

    @classmethod
    def from_str(cls, string: str) -> Category:
        return {
            "SAFE": cls.SAFE,
            "PHISHING": cls.PHISHING,
            "MALWARE": cls.MALWARE,
        }[string.upper()]


class Permission(Enum):
    DOMAINS = "domains"
    URLS = "urls"
