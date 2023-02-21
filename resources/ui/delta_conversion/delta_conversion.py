from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from .utils.calculate_delta_values import CaclulateDeltaValues


class DeltaWindow(QWidget):
    def __init__(self, diag):
        super().__init__()
        self.diag = diag
        self.setObjectName("myParentWidget")
        self.create_widget_objects()
        self.create_layout()

        self.button_calculate.clicked.connect(self.calculate_delta_values)

    # Creates widget objects
    def create_widget_objects(self):
        self.label_title = QLabel("Give motor nameplate values\n(Delta 230V)")
        self.label_title.setObjectName("DeltaGuiTitle")

        self.Label_rpm = QLabel("Motor nameplate rpm")
        self.qline_rpm = QLineEdit("")
        self.rpm_validator = QIntValidator(self.qline_rpm)
        self.rpm_validator.setRange(0, 10000)
        self.qline_rpm.setValidator(self.rpm_validator)

        self.Label_power = QLabel("Motor nameplate power (kW)")
        self.qline_power = QLineEdit("")
        self.power_validator = QDoubleValidator(self.qline_rpm)
        self.power_validator.setRange(0, 100, 2)
        self.qline_power.setValidator(self.power_validator)

        self.Label_amps = QLabel("Motor nameplate amps")
        self.qline_amps = QLineEdit("")
        self.amps_validator = QDoubleValidator(self.qline_amps)
        self.amps_validator.setRange(0, 100, 2)
        self.qline_amps.setValidator(self.amps_validator)

        self.Label_frequency = QLabel("Motor nameplate frequency")
        self.qline_frequency = QLineEdit("")
        self.freq_validator = QIntValidator(self.qline_amps)
        self.freq_validator.setRange(0, 99)
        self.qline_frequency.setValidator(self.freq_validator)

        self.Label_poles = QLabel("Number of poles pairs")
        self.qline_poles = QLineEdit("")
        self.pole_validator = QIntValidator(self.qline_amps)
        self.pole_validator.setRange(0, 99)
        self.qline_poles.setValidator(self.pole_validator)

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
        try:
            self.Label_rpm_result.setText("RPM: " + CaclulateDeltaValues.rpm(int(
                self.qline_rpm.text()), int(self.qline_poles.text()), int(self.qline_frequency.text())))

            self.Label_amps_result.setText(
                "Amps: " + self.qline_amps.text() + " A")

            self.Label_frequency_result.setText(
                "Frequency: " + CaclulateDeltaValues.multiple_by_sqr3(int(self.qline_frequency.text().replace(",", "."))) + " Hz")

            self.Label_power_result.setText(
                "Power: " + CaclulateDeltaValues.multiple_by_sqr3(float(self.qline_power.text().replace(",", "."))) + " kW")

        except:
            self.diag.show()
