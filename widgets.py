import krita
from .run_client import start_client

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from .client import get_data_manager, ClientComputedImage, ClientLayerImage


class PythonReferenceDialog(QDialog):
    def __init__(self, parent):

        super(PythonReferenceDialog, self).__init__(parent=parent)
        self.setModal(True)
        self.setWindowTitle('Neural Style Transfer Plugin')

        # The general layout
        outer_layout = QVBoxLayout()
        selector_widget = QWidget()
        selector_layout = QHBoxLayout()

        selector_layout.addWidget(self.get_layer_selector(title='content'))
        selector_layout.addWidget(self.get_layer_selector(title='style'))
        selector_layout.addWidget(self.get_layer_selector(title='output'))

        selector_widget.setLayout(selector_layout)
        outer_layout.addWidget(selector_widget)
        q = QPushButton("Run", self)
        q.clicked.connect(lambda x: self.close())
        outer_layout.addWidget(q)

        self.setLayout(outer_layout)
        self.resize(200, 100)

    def get_layer_selector(self, title=""):
        node = QWidget(self)
        layout = QVBoxLayout()

        label = QLabel(node)
        label.setText(title)
        layout.addWidget(label)

        content = QComboBox(node)
        for l in self.get_all_layers():
            content.addItem(l)
        layout.addWidget(content)

        node.setLayout(layout)
        return node

    def get_all_layers(self):
        for child in krita.Krita.instance().activeDocument().rootNode(
        ).childNodes():
            yield child.name()


class CelestiaPrimeExtension(krita.Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        start_client()

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
        data_manager = get_data_manager()
        print("Setting up images...")
        content = ClientLayerImage(data_manager, {
            "layer_name":"content",
            "x0": 0,
            "y0": 0,
            "x_count": 10,
            "y_count": 10,
            "w": 100,
        })
        print(data_manager)
        print(data_manager.images)
        print("Done! Images should auto-sync now")
 