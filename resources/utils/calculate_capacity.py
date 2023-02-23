def capacity_calculation(wrapping_time, conveying_time):
    capacity = round(3600 / (wrapping_time + conveying_time), 2)
    return str(capacity)


if __name__ == "__main__":
    print(capacity_calculation(30, 0))