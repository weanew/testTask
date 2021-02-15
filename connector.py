import json
import asyncio
import websockets
import time
from pprint import pprint


class Connector:

    def __init__(self):
        self.uri = None
        self.__pool_min = 3
        self.__pool_max = 10
        self.__socket_pool = []

    async def __connect_socket(self):
        socket = await websockets.connect(self.uri)
        socket_lst = [socket, 'ready']
        self.__socket_pool.append(socket_lst)
        return socket_lst

    async def __get_ready_socket(self):
        socket = None
        for socket_lst in self.__socket_pool:
            if socket_lst[1] == 'ready':
                socket = socket_lst
                return socket
        if socket is None:
            if len(self.__socket_pool) == self.__pool_max:
                while socket is None:
                    for socket_lst in self.__socket_pool:
                         if socket_lst[1] == 'ready':
                            socket = socket_lst
                    await asyncio.sleep(1)
                return socket
            elif len(self.__socket_pool) < self.__pool_max:
                socket_lst = await self.__connect_socket()
                return socket_lst

    async def connect(self, uri: str) -> "Connector":
        self.uri = uri
        if len(self.__socket_pool) == 0:
            await asyncio.gather(*[self.__connect_socket() for _ in range(0, self.__pool_min)])
        else:
            raise Exception("Connection already exists.")
        return self

    async def disconnect(self):
        if len(self.__socket_pool) != 0:
            for socket_tuple in self.__socket_pool:
                await socket_tuple[0].close()
            self.__socket_pool = []
        else:
            raise Exception("Connection does not exist.")

    async def call(self, **kwargs) -> str:
        if len(self.__socket_pool) != 0:
            msg = json.dumps(kwargs)
            socket_lst = await self.__get_ready_socket()
            socket_lst[1] = 'busy'
            await socket_lst[0].send(msg)
            response = await socket_lst[0].recv()
            socket_lst[1] = 'ready'
            return response
        else:
            raise Exception("Connection does not exist.")


async def start_con(uri: str):
    connector = Connector()
    connector = await connector.connect(uri)
    results = await asyncio.gather(*[connector.call(arg1=234, art2='abcd', arg3=5) for _ in range(0, 1000)])
    await connector.disconnect()
    pprint(results)
    return results



# if __name__ == '__main__':
#     uri = 'ws://localhost:8765'
#     t0 = time.time()
#     asyncio.get_event_loop().run_until_complete(start_con(uri))
#     print(f'total_time: {time.time() - t0} sec')
