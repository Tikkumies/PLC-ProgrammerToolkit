from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QDoubleValidator
from ...utils.calculate_capacity import capacity_calculation



class CapacityWindow(QWidget):
    def __init__(self, diag):
        super().__init__()
        self.diag = diag
        self.setObjectName("myParentWidget")
        self.create_widget_objects()
        self.create_layout()

        self.button_calculate.clicked.connect(self.calculate_capacity)

    # Creates widget objects
    def create_widget_objects(self):
        self.label_title = QLabel("Capacity calculator")
        self.label_title.setObjectName("DeltaGuiTitle")

        self.label_wrapping_time = QLabel("Wrapping time (s)")
        self.qline_wrapping_time = QLineEdit("")
        self.wrapping_validator = QDoubleValidator(self.qline_wrapping_time)
        self.wrapping_validator.setRange(0, 10000, 2)
        self.qline_wrapping_time.setValidator(self.wrapping_validator)

        self.label_conveying_time = QLabel("Conveying time (s)")
        self.qline_conveying_time = QLineEdit("")
        self.conveying_validator = QDoubleValidator(self.qline_conveying_time)
        self.conveying_validator.setRange(0, 100, 2)
        self.qline_conveying_time.setValidator(self.conveying_validator)

        self.label_placeholder = QLabel("")
        self.label_capacity = QLabel("")

        self.button_calculate = QPushButton("Calculate")

    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.label_title, 0, 0)
        self.layout.addWidget(self.label_wrapping_time, 1, 0)
        self.layout.addWidget(self.qline_wrapping_time, 2, 0)

        self.layout.addWidget(self.label_conveying_time, 3, 0)
        self.layout.addWidget(self.qline_conveying_time, 4, 0)

        self.layout.addWidget(self.label_placeholder, 5, 0)

        self.layout.addWidget(self.label_capacity, 6, 0)
        self.layout.addWidget(self.button_calculate, 7, 0)

        self.layout.setRowStretch(5, 5)

        self.setLayout(self.layout)

    def calculate_capacity(self):
        try:
            self.label_capacity.setText("Capacity: " + capacity_calculation(
                 float(self.qline_wrapping_time.text().replace(",",".")),
                 float(self.qline_conveying_time.text().replace(",","."))) +
                 " pallets per hour")
        except:
            self.diag.show()