import krita

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


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
		q = QPushButton("Run",self)
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
		for child in krita.Krita.instance().activeDocument().rootNode().childNodes():
			yield child.name()