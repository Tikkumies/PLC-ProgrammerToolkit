from PyQt5.QtWidgets import QMainWindow, QMenuBar, QAction, QStackedWidget
from resources.ui.ip_changer.ip_changer import *
from resources.ui.delta_conversion.delta_conversion import *
from resources.ui.capacity.capacity_calculator import *
from resources.ui.open_programs.open_programs import *
from resources.ui.widgets.dialog import Dialog
from .styles import styles


class MainWindow(QMainWindow):
    def __init__(self, ip_window, delta_window, capacity_window, open_programs_window, icon):
        super().__init__()
        self.icon = icon
        self.ip_window = ip_window
        self.delta_window = delta_window
        self.capacity_window = capacity_window
        self.open_programs_window = open_programs_window
        self.setWindowIcon(QIcon(self.icon))
        self.setObjectName("myParentWidget")
        self.setWindowTitle("IP changer")
        # create stacked widget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.ip_window)
        self.stacked_widget.addWidget(self.delta_window)
        self.stacked_widget.addWidget(self.capacity_window)
        self.stacked_widget.addWidget(self.open_programs_window)
        self.setCentralWidget(self.stacked_widget)
        # menubar
        self.menu = QMenuBar()
        self.setMenuBar(self.menu)
        self.file_menu = self.menu.addMenu("&File")
        self.view_menu = self.menu.addMenu("&View")
        self.action_ip_view = QAction("& IP changer", self)
        self.action_ip_view.setCheckable(True)
        self.action_ip_view.setChecked(True)
        self.action_delta_view = QAction("& Delta conversion", self)
        self.action_delta_view.setCheckable(True)
        self.action_capacity_view = QAction("& Capacity calculator", self)
        self.action_capacity_view.setCheckable(True)
        self.action_open_view = QAction("& Open programs", self)
        self.action_open_view.setCheckable(True)
        self.view_menu.addAction(self.action_ip_view)
        self.view_menu.addAction(self.action_delta_view)
        self.view_menu.addAction(self.action_capacity_view)
        self.view_menu.addAction(self.action_open_view)
        # signals
        self.action_ip_view.triggered.connect(self.open_ip_changer)
        self.action_delta_view.triggered.connect(self.open_delta_conversion)
        self.action_capacity_view.triggered.connect(self.open_capacity_calculator)
        self.action_open_view.triggered.connect(self.open_open_programs)

    def open_ip_changer(self):
        self.stacked_widget.setCurrentIndex(0)
        self.setWindowTitle("IP changer")
        self.action_ip_view.setChecked(True)
        self.action_delta_view.setChecked(False)
        self.action_capacity_view.setChecked(False)
        self.action_open_view.setChecked(False)

    def open_delta_conversion(self):
        self.stacked_widget.setCurrentIndex(1)
        self.setWindowTitle("Delta conversion")
        self.action_delta_view.setChecked(True)
        self.action_ip_view.setChecked(False)
        self.action_capacity_view.setChecked(False)
        self.action_open_view.setChecked(False)

    def open_capacity_calculator(self):
        self.stacked_widget.setCurrentIndex(2)
        self.setWindowTitle("Capacity calculator")
        self.action_capacity_view.setChecked(True)
        self.action_delta_view.setChecked(False)
        self.action_ip_view.setChecked(False)
        self.action_open_view.setChecked(False)

    def open_open_programs(self):
        self.stacked_widget.setCurrentIndex(3)
        self.setWindowTitle("Open programs")
        self.action_open_view.setChecked(True)
        self.action_capacity_view.setChecked(False)
        self.action_delta_view.setChecked(False)
        self.action_ip_view.setChecked(False)
