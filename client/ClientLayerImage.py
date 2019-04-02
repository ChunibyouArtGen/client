from sync.images import LayerImage
from sync.images import register_image_class

def get_node_object(layer_name):
    pass


@register_image_class
class ClientLayerImage(LayerImage):
    def __init__(self, data_manager, params):
        super().__init__(data_manager, params)
        self.krita_node = get_node_object(params['layer_name'])

    def scan(self):
        # Scan Krita for updates
        pass

    def handle_update(self, tile_key, data):
        # Write to krita
        pass
