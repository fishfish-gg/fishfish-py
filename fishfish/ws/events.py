from __future__ import annotations

from enum import Enum

from fishfish.ws.models import *


class WebsocketEvents(str, Enum):
    URL_CREATE = "url_create"
    URL_UPDATE = "url_update"
    URL_DELETE = "url_delete"
    DOMAIN_CREATE = "domain_create"
    DOMAIN_UPDATE = "domain_update"
    DOMAIN_DELETE = "domain_delete"

    @classmethod
    def from_string(cls, event_type: str) -> WebsocketEvents:
        """Create the correct event based on the event type.

        Raises
        ------
        ValueError
            Unknown event type
        """
        ctx = getattr(cls, event_type)
        if ctx is None:
            raise ValueError(f"Unknown event type {event_type}")

        return ctx

    def create_model(self, data: dict):
        """Create the correct data model for this event type."""
        factories = {
            WebsocketEvents.URL_CREATE: WSUrlCreate,
            WebsocketEvents.URL_UPDATE: WSUrlUpdate,
            WebsocketEvents.URL_DELETE: WSUrlDelete,
            WebsocketEvents.DOMAIN_CREATE: WSDomainCreate,
            WebsocketEvents.DOMAIN_UPDATE: WSDomainUpdate,
            WebsocketEvents.DOMAIN_DELETE: WSDomainDelete,
        }
        return factories[self].from_dict(data)
