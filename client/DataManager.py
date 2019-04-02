from sync.data_manager import DataManager
import logging
import asyncio
logger = logging.getLogger(__name__)


class ClientDataManager(DataManager):
    async def watch_layers(self):
        while True:
            logger.debug("Scanning layer images...")
            for uuid, image in self.images.items():
                image.scan()

            await asyncio.sleep(2)
