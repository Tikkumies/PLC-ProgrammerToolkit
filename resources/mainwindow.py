from PyQt5.QtWidgets import QMainWindow, QMenuBar, QAction, QStackedWidget
from resources.ui.ip_changer.ip_changer import *
from resources.ui.delta_conversion.delta_conversion import *
from .ui.styles import styles


class MainWindow(QMainWindow):
    def __init__(self, ip_window, test_window):
        super().__init__()
        self.setObjectName("myParentWidget")
        self.setWindowTitle("IP changer")
        self.ip_window = ip_window
        self.test_window = test_window
        # create stacked widget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.ip_window)
        self.stacked_widget.addWidget(self.test_window)
        self.setCentralWidget(self.stacked_widget)
        # menu bar
        self.menu = QMenuBar()
        self.setMenuBar(self.menu)
        file_menu = self.menu.addMenu("&View")
        self.action_ip_view = QAction("&Ip changer", self)
        self.action_test_view = QAction("&Test", self)
        file_menu.addAction(self.action_ip_view)
        file_menu.addAction(self.action_test_view)
        # signals
        self.action_ip_view.triggered.connect(self.open_ip_changer)
        self.action_test_view.triggered.connect(self.open_test)

    def open_ip_changer(self):
        self.stacked_widget.setCurrentIndex(0)
        self.setWindowTitle("IP changer")

    def open_test(self):
        self.stacked_widget.setCurrentIndex(1)
        self.setWindowTitle("Delta conversion")
