import json
import asyncio
import websockets


class Connector:

    def __init__(self):
        self.socket_session = None

    async def connect(self, uri: str) -> "Connector":
        if self.socket_session is None:
            self.socket_session = await websockets.connect(uri).__aenter__()
        else:
            raise Exception("Connection already exists.")
        return self

    async def disconect(self):
        if self.socket_session is not None:
            await self.socket_session.close()
            self.socket_session = None
        else:
            raise Exception("Connection does not exist.")

    async def call(self, **kwargs) -> str:
        if self.socket_session is not None:
            msg = json.dumps(kwargs)
            ws = self.socket_session
            await ws.send(msg)

            response = await ws.recv()
            return response
        else:
            raise Exception("Connection does not exist.")


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
