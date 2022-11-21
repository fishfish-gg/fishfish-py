"""
fishfish-py
-----------
FishFish API library for Python
:copyright: (c) 2022 fishfish.gg
:license: MIT, see LICENSE for more details.
"""

__title__ = "fishfish"
__author__ = "fishfish-gg"
__license__ = "MIT"
__copyright__ = "Copyright 2022 fishfish.gg"
__version__ = "0.1.0"


from .enums import Category, Permission
from .models import URL, APIStatus, Domain, Token
from .exceptions import (
    FishFishException,
    Forbidden,
    Unauthorized,
    ServerError,
    AuthenticatedRoute,
    ObjectDoesntExist,
)
from .fish_http_client import FishHTTPClient
