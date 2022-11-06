class FishFishException(Exception):
    """Base exception for this package."""


class Unauthorized(FishFishException):
    """This request was made lacking the correct authentication."""


class Forbidden(FishFishException):
    """You do not have permissions to execute this action."""


class ServerError(FishFishException):
    """Something went wrong on the servers side."""
