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
from .exceptions import (
    AuthenticatedRoute,
    FishFishException,
    Forbidden,
    ObjectDoesntExist,
    ServerError,
    Unauthorized,
)
from .models import (  # keep this import above the http client import, it will raise an ImportError otherwise. black/isort will do that when ran so don't forget to undo - BeeMoe
    URL,
    APIStatus,
    Domain,
    Token,
)
from .fish_http_client import FishHTTPClient
