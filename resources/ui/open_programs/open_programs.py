from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QPushButton, QGridLayout, QFileDialog, QLineEdit
from ...utils.open_program import open_program

class OpenPrograms(QWidget):
    def __init__(self):
        super().__init__()
        #self.diag = diag
        self.setObjectName("myParentWidget")
        self.create_widget_objects()
        self.create_layout()
        self.file_dialog = QFileDialog()

        self.button_ix.clicked.connect(lambda: self.open_file_dialog(self.qline_ix))
        self.button_lenze.clicked.connect(lambda: self.open_file_dialog(self.qline_lenze))
        self.button_vmware.clicked.connect(lambda: self.open_file_dialog(self.qline_vmware))
        self.button_connect.clicked.connect(lambda: self.open_file_dialog(self.qline_connect))
        self.button_open.clicked.connect(lambda: self.open_programs())

    # Creates widget objects
    def create_widget_objects(self):
        self.label_title = QLabel("Open programs")
        self.label_title.setObjectName("DeltaGuiTitle")

        self.Label_ix = QLabel("IX Developer")
        self.check_ix = QCheckBox()
        self.button_ix = QPushButton("...")
        self.qline_ix = QLineEdit("")

        self.Label_lenze = QLabel("Lenze Engineer")
        self.check_lenze = QCheckBox()
        self.button_lenze = QPushButton("...")
        self.qline_lenze = QLineEdit("")

        self.Label_vmware = QLabel("WMware")
        self.check_vmware = QCheckBox()
        self.button_vmware = QPushButton("...")
        self.qline_vmware = QLineEdit("")

        self.Label_connect = QLabel("Connect")
        self.check_connect = QCheckBox()
        self.button_connect = QPushButton("...")
        self.qline_connect = QLineEdit("")

        self.label_placeholder = QLabel("")

        self.button_open = QPushButton("Open")

    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.label_title, 0, 0)

        self.layout.addWidget(self.Label_ix, 1, 0)
        self.layout.addWidget(self.check_ix, 1, 1)
        self.layout.addWidget(self.button_ix, 1, 3)
        self.layout.addWidget(self.qline_ix, 1, 2, 1, 1)

        self.layout.addWidget(self.Label_lenze, 2, 0)
        self.layout.addWidget(self.check_lenze, 2, 1)
        self.layout.addWidget(self.button_lenze, 2, 3)
        self.layout.addWidget(self.qline_lenze, 2, 2, 1, 1)

        self.layout.addWidget(self.Label_vmware, 3, 0)
        self.layout.addWidget(self.check_vmware, 3, 1)
        self.layout.addWidget(self.button_vmware, 3, 3)
        self.layout.addWidget(self.qline_vmware, 3, 2, 1, 1)

        self.layout.addWidget(self.Label_connect, 4, 0)
        self.layout.addWidget(self.check_connect, 4, 1)
        self.layout.addWidget(self.button_connect, 4, 3)
        self.layout.addWidget(self.qline_connect, 4, 2, 1, 1)

        self.layout.addWidget(self.label_placeholder,6, 0)
        self.layout.setRowStretch(5, 5)

        self.layout.addWidget(self.button_open, 5, 0)
        self.layout.setRowStretch(6, 5)

        self.setLayout(self.layout)

    def open_file_dialog(self, line_edit_text):
        line_edit_text.setText(self.file_dialog.getOpenFileName()[0])

    def open_programs(self):
        if self.check_ix.checkState():
            open_program(self.qline_ix.text())
        if self.check_lenze.checkState():
            open_program(self.qline_lenze.text())
        if self.check_vmware.checkState():
            open_program(self.qline_vmware.text())
        if self.check_connect.checkState():
            open_program(self.qline_connect.text())

    

        
