from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class Dialog(QDialog):
    def __init__(self, name='', descr='', full='', parent=None):
        super().__init__(parent)
        self.setWindowTitle('Task')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()

        self.nameField = QLineEdit()
        formLayout.addRow('Name:', self.nameField)
        self.descrField = QLineEdit()
        formLayout.addRow('Description:', self.descrField)
        self.fullField = QPlainTextEdit()
        formLayout.addRow('Problem:', self.fullField)

        self.nameField.insert(name)
        self.descrField.insert(descr)
        self.fullField.appendPlainText(full)

        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.rejected.connect(self.reject)
        btns.accepted.connect(self.accept)

        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

    def accept(self):
        self.name = self.nameField.text()
        self.descr = self.descrField.text()
        self.problem = self.fullField.toPlainText()
        self.done(0)

    def reject(self):
        self.done(1)
