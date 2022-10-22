from enum import Enum


class Category(Enum):
    SAFE = "safe"
    PHISHING = "phishing"
    MALWARE = "malware"


class Permission(Enum):
    DOMAINS = "domains"
    URLS = "urls"
