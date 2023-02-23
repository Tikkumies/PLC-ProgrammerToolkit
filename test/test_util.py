import unittest
import sys
import os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from resources.utils.calculate_delta_values import CaclulateDeltaValues
from resources.utils.handle_ip import get_network_adapter_data
from PyQt5.QtWidgets import QDialog, QWidget, QApplication

class TestUtils(unittest.TestCase):
    def test_delta_calc(self):
        self.assertEqual(CaclulateDeltaValues.rpm(
                        1730, 2, 60), "3047.69")
        
    def test_get_network_adapter_data(self):
        self.assertIn(get_network_adapter_data("name"), "Ehternet")
        


