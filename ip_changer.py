import sys 
import subprocess
import ipaddress
import os
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
    def __init__(self, diag):
        self.diag = diag
        super().__init__()
        self.setWindowTitle("IP Changer")
        self.setFixedSize(250,300)

        self.create_widget_objects()
        self.layout_methods()

        self.button_change_static.clicked.connect(lambda: self.change_ip("static"))
        self.button_change_dhcp.clicked.connect(lambda: self.change_ip("dhcp"))

    # Creates widget objects   
    def create_widget_objects(self):
        self.Label_name = QLabel("Network name")
        self.qcombo_name = QComboBox(self)
        adapters = self.get_network_adapter_names()
        for adapter in adapters:
            self.qcombo_name.addItem(adapter)


        self.Label_ip = QLabel("IP address")
        self.qline_ip = QLineEdit("10.0.0.223")

        self.Label_mask = QLabel("Subnet mask")
        self.qline_mask = QLineEdit("255.255.255.0")

        self.Label_gateway = QLabel("Default gateway")
        self.qline_gateway = QLineEdit("0.0.0.0")

        self.button_change_static = QPushButton("Set static IP")

        self.button_change_dhcp = QPushButton("Set to DHCP")

    # layout related stuff
    def layout_methods(self):
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

        self.setLayout(self.layout)   

    def get_network_adapter_names(self):
        command = "ipconfig"
        completed_process = (subprocess.run(command, capture_output=True))
        string = str(completed_process.stdout)
        print(string)
        adapter_list = []
        x = True
        while x == True:
            start = string.find("Ethernet adapter ") + len("Ethernet adapter ")
            end = string.find(":",start)

            if string.find("Ethernet adapter") == -1:
                x = False
            else:
                adapter_list.append(string[start:end])
                string = string[end:]

        print(adapter_list)
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

if __name__ == '__main__':
    my_path = os.path.abspath(os.path.dirname(__file__))
    app = QApplication(sys.argv)
    app.setStyleSheet(GLOBAL_STYLE)
    dialog = Dialog()
    window = Window(dialog)

    window.show()
    sys.exit(app.exec_())

