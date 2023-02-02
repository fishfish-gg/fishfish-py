import asyncio
import datetime
import json
import logging
import traceback
from typing import Optional

import httpx
import websockets as websockets

from fishfish import Token, Unauthorized
from fishfish.ws import WebsocketEvents

log = logging.getLogger(__name__)


class FishWebsocket:
    def __init__(self, api_key: str):
        self.__refresh_token: Optional[str] = api_key
        self.__current_session_token: Optional[Token] = None
        self._listeners: dict[WebsocketEvents, list] = {
            WebsocketEvents.URL_CREATE: [],
            WebsocketEvents.URL_UPDATE: [],
            WebsocketEvents.URL_DELETE: [],
            WebsocketEvents.DOMAIN_CREATE: [],
            WebsocketEvents.DOMAIN_UPDATE: [],
            WebsocketEvents.DOMAIN_DELETE: [],
        }
        self._error_handler = None

    def _set_session_key(self):
        if (
            self.__current_session_token
            and not self.__current_session_token.has_expired
        ):
            return

        r = httpx.post(
            "https://api.fishfish.gg/v1/users/@me/tokens",
            headers={"Authorization": self.__refresh_token},
        )
        if r.status_code == 401:
            raise Unauthorized("Your provided FishFish token is invalid.")

        data = r.json()
        token = data["token"]
        expires = datetime.datetime.fromtimestamp(data["expires"])
        self.__current_session_token = Token(token, expires)

    async def _process_event(self, data):
        try:
            event_type: WebsocketEvents = WebsocketEvents.from_string(data["type"])
            model = event_type.create_model(data["data"])
            iters = [coro(model) for coro in self._listeners[event_type]]
            if iters:
                await asyncio.gather(*iters)
        except Exception as e:
            if not self._error_handler:
                log.error("Attempting to process %s threw %s", str(e), str(e))
                log.error("%s", "".join(traceback.format_exception(e)))
                return

            asyncio.create_task(self._error_handler(e))

    async def _ws_loop(self):
        self._set_session_key()
        async with websockets.connect(
            "wss://api.fishfish.gg/v1/stream/",
            extra_headers={"Authorization": self.__current_session_token.token},
        ) as websocket:
            async for message in websocket:
                asyncio.create_task(self._process_event(json.loads(message)))

    async def start(self) -> asyncio.Task:
        return asyncio.create_task(self._ws_loop())

    def register_listener(self, event: WebsocketEvents, coro):
        """Register a listener for a websocket event.

        Parameters
        ----------
        event: WebsocketEvents
            The event to listen for.
        coro
            An async function or method to call
            when this event is fired.

            The first parameter will be the event data.

        Raises
        ------
        ValueError
            The provided function or method was not async.
        """
        if not asyncio.iscoroutinefunction(coro):
            raise ValueError(
                f"The provided value for 'coro' must be a coroutine function."
            )

        self._listeners[event].append(coro)

    def register_error_handler(self, coro):
        """Register a function to handle errors.

        Parameters
        ----------
        coro
            An async function or method to call
            when an error occurs.

            The first parameter will be the exception.
        """
        self._error_handler = coro
