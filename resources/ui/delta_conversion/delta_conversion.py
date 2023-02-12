from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout


class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("myParentWidget")
        self.create_widget_objects()
        self.create_layout()

    # Creates widget objects
    def create_widget_objects(self):
        self.label_title = QLabel("Give motor nameplate values")

        self.Label_rpm = QLabel("Motor nameplate rpm")
        self.qcombo_rpm = QLineEdit(self)

        self.Label_power = QLabel("Motor nameplate power")
        self.qline_power = QLineEdit("ip")

        self.Label_amps = QLabel("Motor nameplate amps")
        self.qline_amps = QLineEdit("")

        self.button_calculate = QPushButton("Calculate")

    # layout related stuff

    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.label_title, 0, 0)
        self.layout.addWidget(self.Label_rpm, 1, 0)
        self.layout.addWidget(self.qcombo_rpm, 2, 0)

        self.layout.addWidget(self.Label_power, 3, 0)
        self.layout.addWidget(self.qline_power, 4, 0)

        self.layout.addWidget(self.Label_amps, 5, 0)
        self.layout.addWidget(self.qline_amps, 6, 0)

        self.layout.addWidget(self.button_calculate, 7, 0)

        self.setLayout(self.layout)
