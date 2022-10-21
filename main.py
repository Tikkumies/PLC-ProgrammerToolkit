import sys 
import subprocess
import ipaddress
import os
from PyQt5.QtWidgets import (QApplication, QPushButton, QGridLayout, QWidget, QLineEdit, QLabel) 


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
    """

class Window(QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setWindowTitle("IP changer")
        self.setFixedSize(250,300)

        self.create_widget_objects()
        self.layout_methods()

        self.button_change.clicked.connect(self.change_ip)

    # Creates widget objects   
    def create_widget_objects(self):
        self.Label_name = QLabel("Network name")
        self.qline_name = QLineEdit("Ethernet")

        self.Label_ip = QLabel("IP address")
        self.qline_ip = QLineEdit("10.0.0.223")

        self.Label_mask = QLabel("Subnet mask")
        self.qline_mask = QLineEdit("255.255.255.0")

        self.Label_gateway = QLabel("Default gateway")
        self.qline_gateway = QLineEdit("0.0.0.0")

        self.button_change = QPushButton("Ok")

    # layout related stuff
    def layout_methods(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.Label_name,0,0)
        self.layout.addWidget(self.qline_name,1,0)

        self.layout.addWidget(self.Label_ip,2,0)  
        self.layout.addWidget(self.qline_ip,3,0)  

        self.layout.addWidget(self.Label_mask,4,0)
        self.layout.addWidget(self.qline_mask,5,0)

        self.layout.addWidget(self.Label_gateway,6,0)
        self.layout.addWidget(self.qline_gateway,7,0)

        self.layout.addWidget(self.button_change,8,0)      

        self.setLayout(self.layout)   

    # Changes network adapter settings
    def change_ip(self):
        name = self.qline_name.text()
        ip = self.qline_ip.text()
        mask = self.qline_mask.text()
        gateway = self.qline_gateway.text()
        try:
            ipaddress.ip_address(ip)
            ipaddress.ip_address(mask)
            ipaddress.ip_address(gateway)
            with open ("Scripts\ChangeIP.bat", "w") as bat_file:
                bat_file.write("@echo off\n" + "netsh interface ip set address " + name + " static " + ip + " " + mask + " " + gateway)
            subprocess.run("Scripts\ChangeIP.bat")
        except ValueError:
            print("Please enter valid IP address, Subnet mask, and Default gateway")

if __name__ == '__main__':
    my_path = os.path.abspath(os.path.dirname(__file__))
    app = QApplication(sys.argv)
    app.setStyleSheet(GLOBAL_STYLE)
    window = Window()
    window.show()
    sys.exit(app.exec_())

