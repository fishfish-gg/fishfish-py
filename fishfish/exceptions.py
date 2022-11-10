from typing import Optional, Dict


class FishFishException(Exception):
    """Base exception for this package."""

    def __init__(self, message: Optional[str] = None):
        self.message: str = message or self.__doc__

    def __str__(self):
        return self.message


class Unauthorized(FishFishException):
    """This request was made lacking the correct authentication."""


class Forbidden(FishFishException):
    """You do not have permissions to execute this action."""


class ObjectDoesntExist(FishFishException):
    """The requested object does not exist."""


class ServerError(FishFishException):
    """Something went wrong on the servers side."""
