import asyncio
import os

from fishfish.ws import FishWebsocket, models, WebsocketEvents


async def on_domain_create(data: models.WSDomainCreate):
    print(f"{data.domain} was just created")


async def on_error(error: Exception):
    raise error


async def main():
    ws: FishWebsocket = FishWebsocket(os.environ["API_KEY"])
    ws.register_error_handler(on_error)
    ws.register_listener(WebsocketEvents.DOMAIN_CREATE, on_domain_create)

    task = await ws.start()
    await task  # Run until complete


asyncio.run(main())
