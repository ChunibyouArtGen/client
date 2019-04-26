import krita

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from sync.client import ClientLayerImage, ClientComputedImage, utils

class FNSTDialog(QDialog):
    def __init__(self, parent, client):

        self.client = client
        super().__init__(parent=parent)
        self.setModal(True)
        self.setWindowTitle('Neural Style Transfer Plugin')

        outer_layout = self.get_selector_layout()

        self.setLayout(outer_layout)
        self.resize(300, 150)

    def get_selector_layout(self):
                # The general layout
        outer_layout = QVBoxLayout()
        selector_widget = QWidget()
        selector_layout = QHBoxLayout()

        content_selector, content_layer = self.get_layer_selector(title='content')
        style_selector, style_layer = self.get_model_selector(title='style')
        output_selector, output_layer = self.get_layer_selector(title='output')

        selector_layout.addWidget(content_selector)
        selector_layout.addWidget(style_selector)
        selector_layout.addWidget(output_selector)

        selector_widget.setLayout(selector_layout)
        outer_layout.addWidget(selector_widget)
        q = QPushButton("Run", self)
        q.clicked.connect(lambda:self.compute(content_layer.currentText(), style_layer.currentText(), output_layer.currentText()))
        outer_layout.addWidget(q)
        return outer_layout
    
    
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
    
    def get_model_selector(self, title=""):
        node = QWidget(self)
        layout = QVBoxLayout()

        label = QLabel(node)
        label.setText(title)
        layout.addWidget(label)

        content = QComboBox(node)
        for l in ['mosaic', 'candy', 'rain_princess', 'udnie']:
            content.addItem(l)
        layout.addWidget(content)

        node.setLayout(layout)
        return (node, content) 

    def get_all_layers(self):
        for child in krita.Krita.instance().activeDocument().rootNode(
        ).childNodes():
            yield child.name()

    def compute(self, content_layer, model_id, output_layer):
        print("Setting up images...")
        print("Printing Selector values")
        content_node = utils.get_node_object("content")
        style_node = utils.get_node_object("style")

        content = ClientLayerImage(
            self.client.data_manager, {
                "layer_name": str(content_layer),
                "x0": 0,
                "y0": 0,
                "x_count": 4,
                "y_count": 4,
                "w": 900,
            })
        
        comp = ClientComputedImage(
            self.client.data_manager, {
                "layer_name": str(output_layer),
                "x0": 0,
                "y0": 800,
                "x_count": 4,
                "y_count": 4,
                "w": 900,
                "model_key": "fastnst",
                "inputs": {
                    "content": content,
                    "style": model_id
                }
            })

        self.client.run_coroutine(content.register_self())
        self.client.run_coroutine(comp.register_self())
        print(self.client.data_manager.images)
        print("Done! Images should auto-sync now")
        

