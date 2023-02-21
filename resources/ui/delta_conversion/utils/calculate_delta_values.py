import math


class CaclulateDeltaValues:
    @staticmethod
    def rpm(nameplate_rpm, pole_pairs, frequency):
        motor_rpm = round((math.sqrt(3) * frequency * 60 / 2) -
                          (frequency * 60 / pole_pairs - nameplate_rpm), 2)
        return str(motor_rpm)

    def multiple_by_sqr3(power_or_frequency):
        # Calculation for motor power and frequency
        result = round(math.sqrt(3) * power_or_frequency, 2)
        return str(result)
