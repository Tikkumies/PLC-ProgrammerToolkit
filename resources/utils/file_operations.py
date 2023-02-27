import os, shutil

class FileOperations:
    @staticmethod
    def find_path(file_name: str, dir_path: str):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file_name in file:
                    path = root + '\\' + file
        return path
        


if __name__ == "__main__":
    dir_path = r"C:\Users\Mikko\Documents\hakutesti\ITW-haloila"
    destination = r"C:\Users\Mikko\Desktop\\"
    file_path = FileOperations.find_path("510445", dir_path)
    shutil.copyfile(file_path, (destination + "510445.pdf"))



