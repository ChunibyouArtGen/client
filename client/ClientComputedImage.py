from sync.images import ComputedImage
from sync.images import register_image_class


def get_node_object(layer_name):
    pass


@register_image_class
class ClientComputedImage(ComputedImage):
    def __init__(self, data_manager, params):
        super().__init__(data_manager, params)
        if 'layer_name' in params:
            self.krita_node = get_node_object(params['layer_name'])


    def handle_update(self, tile_key, data):
        if self.krita_node:
            writa_krita_data_oiasjndolasnmd()
        
        self.task_runner.schedule_compute(self)