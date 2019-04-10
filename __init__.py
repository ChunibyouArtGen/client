import krita

from .widgets import PythonReferenceDialog
from .run_client import run_client


class PythonReferenceExtension(krita.Extension):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        run_client()


    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(
            'nst', 'Neural Style Transfer Plugin', 'tools/scripts')
        action.triggered.connect(self.nst_plugin)

    def nst_plugin(self):
        dlg = PythonReferenceDialog(
            parent=self.parent.activeWindow().qwindow())
        dlg.show()
        dlg.activateWindow()


krita_instance = krita.Krita.instance()
krita_instance.addExtension(PythonReferenceExtension(krita_instance))