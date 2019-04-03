from sync.images import LayerImage
from sync.images import register_image_class
from .utils import *

def get_node_object(layer_name):
    pass


@register_image_class
class ClientLayerImage(LayerImage):
    def __init__(self, data_manager, params):
        super().__init__(data_manager, params)
        self.krita_node = get_node_object(params['layer_name'])

    def scan(self):
        # Scan Krita for updates

        activeDocument = getActiveDocument()
        childNode = getChildNodes(activeDocument)
        imageData = grabImage(childNode, 0, 0, 400, 400)
        imageDataNumpyFormat = get_image_to_numpy(imageData)
        LayerImage().send_updates(imageDataNumpyFormat)

    def handle_update(self, tile_key, data):
        # Write to krita
        pass
