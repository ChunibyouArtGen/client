from sync.images import LayerImage
from sync.images import register_image_class
from .utils import get_node_object, grab_image
import logging
logger = logging.getLogger(__name__)

@register_image_class
class ClientLayerImage(LayerImage):
    def __init__(self, data_manager, params):
        super().__init__(data_manager, params)

    def scan(self):
        logger.debug("Scanning image on layer {}".format(self.params['layer_name']))
        # Scan Krita for updates
        self.krita_node = get_node_object(self.params['layer_name'])

        new_data = grab_image(self.krita_node, self.params['x0'], self.params['y0'], self.params['x_count']*self.params['w'], self.params['y_count']*self.params['w'])
        
        return self.update_data(new_data)

    def handle_update(self, tile_key, data):
        # Don't do anything, since this class is input-only
        pass
