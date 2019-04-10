from .client.DataManager import ClientDataManager
from sync import init_logging

import asyncio
import websockets
import logging
from threading import Thread

logger = logging.getLogger()


async def start():
    init_logging()
    ws = await websockets.connect("ws://localhost:8765")
    data_manager = ClientDataManager(ws)
    logger.debug("Client init complete")
    for i in range(10):
        await data_manager.send_image_definition({
            'type': 'layer',
            'uuid': i,
            'params': {
                'layer_name': 'layer1',
                'x0': 0,
                'y0': 0,
                'x_count': 10,
                'y_count': 10,
                'w': 100
            }
        })
        await asyncio.sleep(1)

    await asyncio.gather(data_manager.channel.listen(),
                         data_manager.watch_layers())


def run_client():
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.ensure_future(start())
    asyncio.get_event_loop().run_forever()


def start_client():
    t = Thread(target=run_client, name='celestiaprime')
    t.start()


if __name__ == "__main__":
    start_client()