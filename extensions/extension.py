from .dialog import PythonReferenceDialog
import krita
from sync.client import ClientLayerImage, ClientComputedImage

class ClientExtension(krita.Extension):
    def __init__(self, parent, client):
        super().__init__(parent)
        self.parent = parent
        self.client = client

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction('nst', 'Neural Style Transfer Plugin',
                                     'tools/scripts')
        action.triggered.connect(self.nst_plugin)

        action = window.createAction('demo', 'Demo', 'tools/scripts')
        action.triggered.connect(self.demo)

    def nst_plugin(self):
        dlg = PythonReferenceDialog(
            parent=self.parent.activeWindow().qwindow())
        dlg.show()
        dlg.activateWindow()

    def demo(self):
        print("Setting up images...")
        content = ClientLayerImage(
            self.client.data_manager, {
                "layer_name": "content",
                "x0": 0,
                "y0": 0,
                "x_count": 10,
                "y_count": 10,
                "w": 100,
            })
        content = ClientLayerImage(
            self.client.data_manager, {
                "layer_name": "content",
                "x0": 100,
                "y0": 1000,
                "x_count": 10,
                "y_count": 10,
                "w": 200
            })
        self.client.run_coroutine(content.register_self())
        print(self.client.data_manager)
        print(self.client.data_manager.images)
        print("Done! Images should auto-sync now")
