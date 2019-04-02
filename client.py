from client.DataManager import ClientDataManager
from sync import init_logging

import asyncio
import websockets
import logging

logger = logging.getLogger()

init_logging()


async def start():
    ws = await websockets.connect("ws://localhost:8765")
    data_manager = ClientDataManager(ws)
    logger.debug("Client init complete")
    for i in range(10):
        await data_manager.send_image_definition({
            'type': 'layer',
            'uuid': i,
            'params': {
                'layer_name': 'layer1'
            }
        })
        await asyncio.sleep(1)

    await asyncio.gather(data_manager.channel.listen(),
                         data_manager.watch_layers())


def run_client():
    asyncio.get_event_loop().run_until_complete(start())
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    run_client()
