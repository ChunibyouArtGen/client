from .dialog import PythonReferenceDialog
from .fnst import FNSTDialog
import krita
from sync.client import ClientComputedImage, ClientLayerImage
from krita import QByteArray
# from sync.client import ClientLayerImage, ClientComputedImage, utils

class ClientExtension(krita.Extension):
    def __init__(self, parent, client):
        super().__init__(parent)
        self.parent = parent
        self.client = client

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction('adain_ui', 'Realtime Style Transfer',
                                     'tools/scripts')
        action.triggered.connect(self.adain_ui)
        
        action = window.createAction('fnst_ui', 'Fast Neural Style Transfer',
                                     'tools/scripts')
        action.triggered.connect(self.fnst_ui)

        action = window.createAction('nst', 'Fast-NST',
                                     'tools/scripts/demo')
        action.triggered.connect(self.demo_fastnst)

        action = window.createAction('adain', 'AdaIN', 'tools/scripts/demo')
        action.triggered.connect(self.demo_adain)

    def adain_ui(self):
        dlg = PythonReferenceDialog(
            parent=self.parent.activeWindow().qwindow(), client=self.client)
        dlg.show()
        dlg.activateWindow()

    def fnst_ui(self):
        dlg = FNSTDialog(
            parent=self.parent.activeWindow().qwindow(), client=self.client)
        dlg.show()
        dlg.activateWindow()

    def demo_adain(self):
        print("Setting up images...")
        content = ClientLayerImage(
            self.client.data_manager, {
                "layer_name": "content",
                "x0": 0,
                "y0": 0,
                "x_count": 4,
                "y_count": 4,
                "w": 900,
            })
        style = ClientLayerImage(
            self.client.data_manager, {
                "layer_name": "style",
                "x0": 0,
                "y0": 0,
                "x_count": 2,
                "y_count": 2,
                "w": 300
            })
        comp = ClientComputedImage(
            self.client.data_manager, {
                "layer_name": "output",
                "x0": 0,
                "y0": 0,
                "x_count": 4,
                "y_count": 4,
                "w": 900,
                "model_key": "adain",
                "inputs": {
                    "content": content,
                    "style": style
                }
            })
        self.client.run_coroutine(content.register_self())
        self.client.run_coroutine(style.register_self())
        self.client.run_coroutine(comp.register_self())

        print(self.client.data_manager.images)
        print("Done! Images should auto-sync now")


    def demo_fastnst(self):
        print("Setting up images...")
        content = ClientLayerImage(
            self.client.data_manager, {
                "layer_name": "content",
                "x0": 0,
                "y0": 0,
                "x_count": 2,
                "y_count": 2,
                "w": 500,
            })
        comp = ClientComputedImage(
            self.client.data_manager, {
                "layer_name": "output",
                "x0": 10,
                "y0": 500,
                "x_count": 2,
                "y_count": 2,
                "w": 500,
                "model_key": "fastnst",
                "inputs": {
                    "content": content,
                    "style": "mosaic"
                }
            })
        self.client.run_coroutine(content.register_self())
        self.client.run_coroutine(comp.register_self())

        print(self.client.data_manager.images)
        print("Done! Images should auto-sync now")
