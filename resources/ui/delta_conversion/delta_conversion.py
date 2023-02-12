from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QDoubleValidator
from .utils.calculate_delta_values import CaclulateDeltaValues


class DeltaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("myParentWidget")
        self.real_number_validator = QDoubleValidator()
        self.real_number_validator.setRange(0, 1000000)
        self.create_widget_objects()
        self.create_layout()

        self.button_calculate.clicked.connect(self.calculate_delta_values)

    # Creates widget objects
    def create_widget_objects(self):
        self.label_title = QLabel("Give motor nameplate values")

        self.Label_rpm = QLabel("Motor nameplate rpm")
        self.qline_rpm = QLineEdit("1756")
        # self.qcombo_rpm.setValidator(self.real_number_validator)

        self.Label_power = QLabel("Motor nameplate power")
        self.qline_power = QLineEdit("3")
        # self.qline_power.setValidator(self.real_number_validator)

        self.Label_amps = QLabel("Motor nameplate amps")
        self.qline_amps = QLineEdit("5")
        # self.qline_amps.setValidator(self.real_number_validator)

        self.Label_frequency = QLabel("Motor nameplate frequency")
        self.qline_frequency = QLineEdit("50")
        # self.qline_frequency.setValidator(self.real_number_validator)

        self.Label_poles = QLabel("Number of poles pairs")
        self.qline_poles = QLineEdit("2")
        # self.qline_poles.setValidator(self.real_number_validator)

        self.Label_rpm_result = QLabel("")
        self.Label_power_result = QLabel("")
        self.Label_amps_result = QLabel("")
        self.Label_frequency_result = QLabel("")

        self.button_calculate = QPushButton("Calculate")

    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.label_title, 0, 0)
        self.layout.addWidget(self.Label_rpm, 1, 0)
        self.layout.addWidget(self.qline_rpm, 2, 0)

        self.layout.addWidget(self.Label_power, 3, 0)
        self.layout.addWidget(self.qline_power, 4, 0)

        self.layout.addWidget(self.Label_amps, 5, 0)
        self.layout.addWidget(self.qline_amps, 6, 0)

        self.layout.addWidget(self.Label_frequency, 7, 0)
        self.layout.addWidget(self.qline_frequency, 8, 0)

        self.layout.addWidget(self.Label_poles, 9, 0)
        self.layout.addWidget(self.qline_poles, 10, 0)

        self.layout.addWidget(self.Label_rpm_result, 11, 0)
        self.layout.addWidget(self.Label_power_result, 12, 0)
        self.layout.addWidget(self.Label_amps_result, 13, 0)
        self.layout.addWidget(self.Label_frequency_result, 14, 0)

        self.layout.addWidget(self.button_calculate, 15, 0)

        self.setLayout(self.layout)

    def calculate_delta_values(self):
        self.Label_rpm_result.setText("RPM: " + CaclulateDeltaValues.rpm(int(
            self.qline_rpm.text()), int(self.qline_poles.text()), int(self.qline_frequency.text())))

        self.Label_amps_result.setText(
            "Amps: " + self.qline_amps.text() + " A")

        self.Label_frequency_result.setText(
            "Frequency: " + CaclulateDeltaValues.multiple_by_sqr3(int(self.qline_frequency.text())) + " Hz")

        self.Label_power_result.setText(
            "Power: " + CaclulateDeltaValues.multiple_by_sqr3(float(self.qline_power.text())) + " kW")
