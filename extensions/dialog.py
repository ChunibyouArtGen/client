import krita

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from sync.client import ClientLayerImage, ClientComputedImage, utils

class PythonReferenceDialog(QDialog):
    def __init__(self, parent, client):

        self.client = client
        super(PythonReferenceDialog, self).__init__(parent=parent)
        self.setModal(True)
        self.setWindowTitle('Neural Style Transfer Plugin')

        # The general layout
        outer_layout = QVBoxLayout()
        selector_widget = QWidget()
        selector_layout = QHBoxLayout()

        content_selector, content_layer = self.get_layer_selector(title='content')
        style_selector, style_layer = self.get_layer_selector(title='style')
        output_selector, output_layer = self.get_layer_selector(title='output')

        selector_layout.addWidget(content_selector)
        selector_layout.addWidget(style_selector)
        selector_layout.addWidget(output_selector)

        selector_widget.setLayout(selector_layout)
        outer_layout.addWidget(selector_widget)
        q = QPushButton("Run", self)
        q.clicked.connect(lambda:self.compute(content_layer.currentText(), style_layer.currentText(), output_layer.currentText()))
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
        return (node, content) 

    def get_all_layers(self):
        for child in krita.Krita.instance().activeDocument().rootNode(
        ).childNodes():
            yield child.name()

    def compute(self, content_layer, style_layer, output_layer):
        print("Setting up images...")
        print("Printing Selector values")
        content_node = utils.get_node_object("content")
        style_node = utils.get_node_object("style")

        content = ClientLayerImage(
            self.client.data_manager, {
                "layer_name": str(content_layer),
                "x0": 0,
                "y0": 0,
                "x_count": 2,
                "y_count": 2,
                "w": 500,
            })
        style = ClientLayerImage(
            self.client.data_manager, {
                "layer_name": str(style_layer),
                "x0": 100,
                "y0": 100,
                "x_count": 2,
                "y_count": 2,
                "w": 500
            })
        comp = ClientComputedImage(
            self.client.data_manager, {
                "layer_name": str(output_layer),
                "x0": 0,
                "y0": 0,
                "x_count": 2,
                "y_count": 2,
                "w": 500,
                "model_id": "nst",
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
        

