import json

class HandleJson:
    @staticmethod
    def read_json(file):
        with open(file, "r") as read:
            data = (json.load(read))
        return data

    @staticmethod
    def write_json(file, data):
        with open(file, "w") as write:
            json.dump(data, write)