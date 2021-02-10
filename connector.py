import json
import asyncio
import websockets


class Connector:

    def __init__(self):
        self.socket_session = None

    async def connect(self, uri: str) -> "Connector":
        self.socket_session = await websockets.connect(uri).__aenter__()
        return self

    async def disconect(self):
        await self.socket_session.close()
        self.socket_session = None

    async def call(self, **kwargs) -> str:
        msg = json.dumps(kwargs)
        ws = self.socket_session
        await ws.send(msg)

        response = await ws.recv()
        return response


async def run_con(uri: str) -> str:
    connector = Connector()
    connector = await connector.connect(uri)
    response = await connector.call(arg1=234, art2='abcd', arg3=5)
    await connector.disconect()
    print(response)
    return response

# if __name__ == '__main__':
#     uri = 'ws://localhost:8765'
#     asyncio.get_event_loop().run_until_complete(run_con(uri))
