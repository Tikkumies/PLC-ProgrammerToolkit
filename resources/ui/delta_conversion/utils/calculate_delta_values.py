import math


class CaclulateDeltaValues:
    @staticmethod
    def rpm(nameplate_rpm, pole_pairs, frequency):
        motor_rpm = nameplate_rpm - 60 * frequency / pole_pairs
        return motor_rpm

    def multiple_by_sqr3(power_or_frequency):
        # Calculation for motor power and frquency
        math.sqrt()
