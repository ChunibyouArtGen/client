from .ClientComputedImage import ClientComputedImage
from .ClientLayerImage import ClientLayerImage
from .DataManager import ClientDataManager
from sync import init_logging
import websockets
import asyncio
import logging

logger = logging.getLogger(__name__)
data_manager = None

def get_data_manager():
    return data_manager

async def start():
    global data_manager
    init_logging(level=logging.INFO)
    ws = await websockets.connect("ws://localhost:8765")
    data_manager = ClientDataManager(ws)
    print(data_manager)
    logger.info("Client init complete")
    await asyncio.gather(data_manager.channel.listen(),
                    data_manager.watch_layers())

def run_client():
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.ensure_future(start())
    asyncio.get_event_loop().run_forever()


__all__ = ['ClientComputedImage', 'ClientLayerImage', 'start', 'get_data_manager']