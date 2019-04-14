from sync.data_manager import DataManager
import logging
import asyncio
logger = logging.getLogger(__name__)


class ClientDataManager(DataManager):
    async def watch_layers(self):
        while True:
            logger.debug("Scanning layer images...")
            for uuid, image in self.images.items():
                if image.scan():
                    self.recompute_dependencies(image)
 
            await asyncio.sleep(2)

    async def recv_recompute(self, uuid):
        logger.debug("Scheduling recompute for {}".format(uuid))
        
