import sys
import ipaddress
from PyQt5.QtWidgets import (QApplication, QPushButton, QGridLayout, QWidget,
                             QLineEdit, QLabel, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox)
from PyQt5.QtGui import QIcon
import os
from ...utils.handle_ip import IpFunctions
from ...utils.handle_json import read_json, write_json


class Window(QWidget):
    def __init__(self, diag, json_file):
        super().__init__()
        self.diag = diag
        self.jsdon_file = json_file
        self.setObjectName("myParentWidget")
        self.setWindowTitle("IP Changer")
        self.create_widget_objects()
        self.update_field_texts_from_file()
        self.create_layout()

        self.button_change_static.clicked.connect(lambda: IpFunctions.change_ip("static", self.qcombo_name.currentText(), self.qline_ip.text(),
                                                                    self.qline_mask.text(), self.qline_gateway.text(), self.diag))
        self.button_change_dhcp.clicked.connect(
            lambda: IpFunctions.change_ip("dhcp", self.qcombo_name.currentText()))
        self.button_get_current_ip.clicked.connect(
            lambda: self.update_fields_to_current())
        self.qcombo_preset.currentTextChanged.connect(
            lambda: self.update_field_texts_from_file())
        self.button_save_presets.clicked.connect(
            lambda: self.update_json_file())

    # Creates widget objects
    def create_widget_objects(self):
        text = IpFunctions.get_text_from_command_line()
        self.Label_preset = QLabel("Preset")
        self.qcombo_preset = QComboBox(self)
        for preset_number in range(1, 6):
            self.qcombo_preset.addItem("Preset " + str(preset_number))

        self.Label_name = QLabel("Network name")
        self.qcombo_name = QComboBox(self)
        adapters = IpFunctions.get_network_adapter_data("name", text)
        for adapter in adapters:
            self.qcombo_name.addItem(adapter)

        self.Label_ip = QLabel("IP address")
        self.qline_ip = QLineEdit(IpFunctions.get_network_adapter_data("ip", text)[
                                  self.qcombo_name.currentIndex()])

        self.Label_mask = QLabel("Subnet mask")
        self.qline_mask = QLineEdit(IpFunctions.get_network_adapter_data("mask", text)[
                                    self.qcombo_name.currentIndex()])

        self.Label_gateway = QLabel("Default gateway")
        self.qline_gateway = QLineEdit(IpFunctions.get_network_adapter_data("gateway", text)[
                                       self.qcombo_name.currentIndex()])

        self.button_change_static = QPushButton("Set static IP")
        self.button_change_dhcp = QPushButton("Set to DHCP")
        self.button_get_current_ip = QPushButton("Get current IP")
        self.button_save_presets = QPushButton("Save Preset")

    # layout related stuff
    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.Label_preset, 0, 0)
        self.layout.addWidget(self.qcombo_preset, 1, 0)

        self.layout.addWidget(self.Label_name, 2, 0)
        self.layout.addWidget(self.qcombo_name, 3, 0)

        self.layout.addWidget(self.Label_ip, 4, 0)
        self.layout.addWidget(self.qline_ip, 5, 0)

        self.layout.addWidget(self.Label_mask, 6, 0)
        self.layout.addWidget(self.qline_mask, 7, 0)

        self.layout.addWidget(self.Label_gateway, 8, 0)
        self.layout.addWidget(self.qline_gateway, 9, 0)

        self.layout.addWidget(self.button_change_static, 10, 0)
        self.layout.addWidget(self.button_change_dhcp, 11, 0)
        self.layout.addWidget(self.button_get_current_ip, 12, 0)
        self.layout.addWidget(self.button_save_presets, 13, 0)

        self.setLayout(self.layout)

    def update_fields_to_current(self):
        text = IpFunctions.get_text_from_command_line()
        self.qline_ip.setText(IpFunctions.get_network_adapter_data("ip", text)[
                              self.qcombo_name.currentIndex()])
        self.qline_mask.setText(IpFunctions.get_network_adapter_data("mask", text)[
                                self.qcombo_name.currentIndex()])
        self.qline_gateway.setText(IpFunctions.get_network_adapter_data("gateway", text)[
                                   self.qcombo_name.currentIndex()])

    def update_field_texts_from_file(self):
        data = read_json(self.jsdon_file)
        self.qline_ip.setText(
            data[self.qcombo_preset.currentIndex()].get("IP"))
        self.qline_mask.setText(
            data[self.qcombo_preset.currentIndex()].get("Mask"))
        self.qline_gateway.setText(
            data[self.qcombo_preset.currentIndex()].get("Gateway"))

    def update_json_file(self):
        try:
            ipaddress.ip_address(self.qline_ip.text())
            ipaddress.ip_address(self.qline_mask.text())
            ipaddress.ip_address(self.qline_gateway.text())

            data = read_json(self.jsdon_file)

            data[self.qcombo_preset.currentIndex()].update(
                {"IP": self.qline_ip.text()})
            data[self.qcombo_preset.currentIndex()].update(
                {"Mask": self.qline_mask.text()})
            data[self.qcombo_preset.currentIndex()].update(
                {"Gateway": self.qline_gateway.text()})

            write_json(self.jsdon_file, data)

        except:
            self.diag.show()
