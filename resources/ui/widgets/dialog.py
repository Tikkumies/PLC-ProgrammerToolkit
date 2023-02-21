from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon


class Dialog(QDialog):
    def __init__(self, window_title, icon, message):
        super().__init__()
        self.setObjectName("myParentWidget")
        self.setWindowTitle(window_title)
        self.setWindowIcon(QIcon(icon))

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        message = QLabel(message)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
