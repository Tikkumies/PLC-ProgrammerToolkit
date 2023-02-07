import sys 
import subprocess
import ipaddress
import os
import json
from PyQt5.QtWidgets import (QApplication, QPushButton, QGridLayout, QWidget, QLineEdit, QLabel, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox) 

GLOBAL_STYLE = """
    QPushButton {
        font-size: 16px;
        text-align:center;
        }
    QLabel {
        font-size: 16px;
        }
    QLineEdit{
        font-size: 16px;
    }
        QComboBox{
        font-size: 16px;
    }
    """

class Window(QWidget):
    def __init__(self, diag, preset_editor):
        self.diag = diag
        self.preset_editor = preset_editor
        super().__init__()
        self.setWindowTitle("IP Changer")
        self.setFixedSize(250,400)

        self.create_widget_objects()
        self.create_layout()

        self.button_change_static.clicked.connect(lambda: self.change_ip("static"))
        self.button_change_dhcp.clicked.connect(lambda: self.change_ip("dhcp"))
        self.button_get_current_ip.clicked.connect(lambda: self.update_fields_to_current())
        self.button_edit_presets.clicked.connect(lambda: self.open_preset_editor())

    # Creates widget objects   
    def create_widget_objects(self):
        self.Label_name = QLabel("Network name")
        self.qcombo_name = QComboBox(self)
        adapters = self.get_network_adapter_data("name")
        for adapter in adapters:
            self.qcombo_name.addItem(adapter)


        self.Label_ip = QLabel("IP address")
        self.qline_ip = QLineEdit(self.get_network_adapter_data("ip")[self.qcombo_name.currentIndex()])

        self.Label_mask = QLabel("Subnet mask")
        self.qline_mask = QLineEdit(self.get_network_adapter_data("mask")[self.qcombo_name.currentIndex()])

        self.Label_gateway = QLabel("Default gateway")
        self.qline_gateway = QLineEdit(self.get_network_adapter_data("gateway")[self.qcombo_name.currentIndex()])

        self.button_change_static = QPushButton("Set static IP")

        self.button_change_dhcp = QPushButton("Set to DHCP")

        self.button_get_current_ip = QPushButton("Get current IP")

        self.button_edit_presets = QPushButton("Edit Presets")

    # layout related stuff
    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.Label_name,0,0)
        self.layout.addWidget(self.qcombo_name,1,0)

        self.layout.addWidget(self.Label_ip,2,0)  
        self.layout.addWidget(self.qline_ip,3,0)  

        self.layout.addWidget(self.Label_mask,4,0)
        self.layout.addWidget(self.qline_mask,5,0)

        self.layout.addWidget(self.Label_gateway,6,0)
        self.layout.addWidget(self.qline_gateway,7,0)

        self.layout.addWidget(self.button_change_static,8,0)
        self.layout.addWidget(self.button_change_dhcp,9,0)  
        self.layout.addWidget(self.button_get_current_ip,10,0) 
        self.layout.addWidget(self.button_edit_presets)

        self.setLayout(self.layout) 

    def update_fields_to_current(self):
        self.qline_ip.setText(self.get_network_adapter_data("ip")[self.qcombo_name.currentIndex()]) 
        self.qline_mask.setText(self.get_network_adapter_data("mask")[self.qcombo_name.currentIndex()])
        self.qline_gateway.setText(self.get_network_adapter_data("gateway")[self.qcombo_name.currentIndex()])

    def get_network_adapter_data(self, data):
        match data:
            case "name":
                find_start = "Ethernet adapter "
                find_end = ":"
            case "ip":
                find_start = "IPv4 Address. . . . . . . . . . . : "
                find_end = " "
            case "mask":
                find_start = "Subnet Mask . . . . . . . . . . . : "
                find_end = " "
            case "gateway":
                find_start = "Default Gateway . . . . . . . . . : "
                find_end = " "
            case "all":
                pass

        command = "ipconfig"
        completed_process = (subprocess.run(command, capture_output=True))
        string = str(completed_process.stdout).replace("\\n"," ").replace("\\r", " ")
        adapter_list = []
        x = True
        while x == True:
            start = string.find(find_start) + len(find_start)
            end = string.find(find_end, start)

            if string.find(find_start) == -1:
                x = False
            else:
                adapter_list.append(string[start:end])
                string = string[end:]
        return (adapter_list)

    # Changes network adapter settings
    def change_ip(self, mode):
        name = self.qcombo_name.currentText()
        ip = self.qline_ip.text()
        mask = self.qline_mask.text()
        gateway = self.qline_gateway.text()
        command = ""

        try:
            if mode == "static":
                command =  "netsh interface ip set address " + name + " static " + ip + " " + mask + " " + gateway
                # Check for valid IP address
                ipaddress.ip_address(ip)
                ipaddress.ip_address(mask)
                ipaddress.ip_address(gateway)

            elif mode == "dhcp":
                command = "netsh interface ip set address " + name + " dhcp"

            subprocess.run(command)

        except ValueError:
            self.diag.show()

    # Open preset editor
    def open_preset_editor(self):
        preset_editor.show()


class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Incorrect network settings")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        message = QLabel("Incorrect IP address, network mask or default gateway")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class PresetEditor(QWidget):
    def __init__(self, diag):
        super().__init__()
        self.diag = diag
        self.setWindowTitle("Preset editor")
        self.setFixedSize(500,110)
        self.create_widgets()
        self.create_layout()

        self.button_save.clicked.connect(lambda: self.update_json_file())
        self.combo_preset.currentTextChanged.connect(lambda: self.change_edit_field_texts())

    def create_widgets(self):
        self.label_preset = QLabel("Preset")
        self.combo_preset = QComboBox()
        for preset_number in range(1,6): 
            self.combo_preset.addItem("Preset " + str(preset_number))

        self.label_ip = QLabel("IP address")
        self.qline_ip = QLineEdit()

        self.Label_mask = QLabel("Subnet mask")
        self.qline_mask = QLineEdit()

        self.Label_gateway = QLabel("Default gateway")
        self.qline_gateway = QLineEdit()

        self.button_save = QPushButton("Save Presets")

    def create_layout(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.label_preset, 0, 0)
        self.layout.addWidget(self.label_ip, 0, 1)
        self.layout.addWidget(self.Label_mask, 0, 2)
        self.layout.addWidget(self.Label_gateway, 0, 3)

        self.layout.addWidget(self.combo_preset, 1, 0)
        self.layout.addWidget(self.qline_ip, 1, 1)
        self.layout.addWidget(self.qline_mask, 1, 2)
        self.layout.addWidget(self.qline_gateway, 1, 3)

        self.layout.addWidget(self.button_save, 2, 0)

        self.setLayout(self.layout)

    def update_json_file(self):
        try:
            ipaddress.ip_address(self.qline_ip.text())
            ipaddress.ip_address(self.qline_mask.text())
            ipaddress.ip_address(self.qline_gateway.text())

            with open("file.json", "r") as read:
                data = (json.load(read))

            data[self.combo_preset.currentIndex()].update({"IP": self.qline_ip.text()})
            data[self.combo_preset.currentIndex()].update({"Mask": self.qline_mask.text()})
            data[self.combo_preset.currentIndex()].update({"Gateway": self.qline_gateway.text()})

            with open("file.json", "w") as write:
                json.dump(data, write)

            print(data)

        except:
            self.diag.show()

    def change_edit_field_texts(self):
        with open("file.json", "r") as read:
            data = (json.load(read))

        self.qline_ip.setText(data[self.combo_preset.currentIndex()].get("IP"))
        self.qline_mask.setText(data[self.combo_preset.currentIndex()].get("Mask"))
        self.qline_gateway.setText(data[self.combo_preset.currentIndex()].get("Gateway"))

if __name__ == '__main__':
    my_path = os.path.abspath(os.path.dirname(__file__))
    app = QApplication(sys.argv)
    app.setStyleSheet(GLOBAL_STYLE)
    dialog = Dialog()
    preset_editor = PresetEditor(dialog)
    window = Window(dialog, preset_editor)

    window.show()
    sys.exit(app.exec_())

