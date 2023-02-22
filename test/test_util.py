import unittest
import sys
import os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from resources.utils.calculate_delta_values import CaclulateDeltaValues
from resources.utils.handle_ip import change_ip
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
import subprocess


class TestUtils(unittest.TestCase):
    def test_delta_calc(self):
        self.assertEqual(CaclulateDeltaValues.rpm(
            1730, 2, 60), "3047.69")
        
    def test_handle_ip(self):
        self.app = QApplication(sys.argv)
        self.qwidget = QWidget()
        self.dialog = QDialog()
        #self.completed_process = subprocess.run("netsh interface ip set address  static 192.168.0.6 255.255.255, 0.0.0.0")
              
        self.assertIsInstance(type(change_ip("static", name = "Ethernet", ip ="192.168.0.44", 
                                        mask = "255.255.255.0", gateway="0.0.0.0"), 
                                        diag_window = self.dialog ), type(subprocess.run("netsh interface ip set address  static 192.168.0.6 255.255.255, 0.0.0.0")))


