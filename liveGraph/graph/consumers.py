import json
from random import randint
from asyncio import sleep

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        for _ in range(1000):
            await self.send(json.dumps({"value": randint(-20, 20)}))
            await sleep(1)
