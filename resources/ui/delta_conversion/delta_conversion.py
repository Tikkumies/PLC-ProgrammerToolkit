from PyQt5.QtWidgets import QWidget, QComboBox, QLabel, QLineEdit, QPushButton, QGridLayout


class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("myParentWidget")
        self.create_widget_objects()
        self.create_layout()

    # Creates widget objects
    def create_widget_objects(self):

        self.Label_name = QLabel("Test")
        self.qcombo_name = QComboBox(self)

        self.Label_ip = QLabel("Test")
        self.qline_ip = QLineEdit("ip")

        self.Label_mask = QLabel("Test")
        self.qline_mask = QLineEdit("")

        self.Label_gateway = QLabel("Default gateway")
        self.qline_gateway = QLineEdit("")

        self.button_change_dhcp = QPushButton("Set to DHCP")
        self.button_get_current_ip = QPushButton("Get current IP")
        self.button_save_presets = QPushButton("Save Preset")

    # layout related stuff
    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.Label_name, 2, 0)
        self.layout.addWidget(self.qcombo_name, 3, 0)

        self.layout.addWidget(self.Label_ip, 4, 0)
        self.layout.addWidget(self.qline_ip, 5, 0)

        self.layout.addWidget(self.Label_mask, 6, 0)
        self.layout.addWidget(self.qline_mask, 7, 0)

        self.layout.addWidget(self.Label_gateway, 8, 0)
        self.layout.addWidget(self.qline_gateway, 9, 0)

        self.layout.addWidget(self.button_change_dhcp, 11, 0)
        self.layout.addWidget(self.button_get_current_ip, 12, 0)
        self.layout.addWidget(self.button_save_presets, 13, 0)

        self.setLayout(self.layout)
