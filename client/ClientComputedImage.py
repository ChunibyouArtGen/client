from sync.images import ComputedImage
from sync.images import register_image_class
from .utils import get_node_object

@register_image_class
class ClientComputedImage(ComputedImage):
    def __init__(self, data_manager, params):
        super().__init__(data_manager, params)
        if params['layer_name'] not in ['', None, ' ']:
            self.krita_node = get_node_object(params['layer_name'])

    def scan(self):
        # Scan Krita for updates
        pass

    def handle_update(self, tile_key, data):
        # Write to krita
        if self.krita_node:
            self.writekritadatablargg()
