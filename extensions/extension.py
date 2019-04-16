from .dialog import PythonReferenceDialog
from sync.client import ClientComputedImage, ClientLayerImage, Client


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
            self.data_manager, {
                "layer_name": "content",
                "x0": 0,
                "y0": 0,
                "x_count": 10,
                "y_count": 10,
                "w": 100,
            })
        self.client.run_coroutine(content.register())
        print(self.data_manager)
        print(self.data_manager.images)
        print("Done! Images should auto-sync now")
