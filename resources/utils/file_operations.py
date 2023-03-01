import os, shutil

class FileOperations:
    @staticmethod
    def find_path(file_name: str, dir_path: str):
        for root, dirs, files in os.walk(dir_path, topdown=False):
            for file in files:
                if file_name in file:
                    path = root + '\\' + file
                    file_name_out = file
        return path, file_name_out
        

if __name__ == "__main__":
    dir_path = r"\\FSRV05\ElecBase$\Base Software\Octopus\PLC\Allen Bradley\New B,S and T"
    destination = r"C:\Users\makelamm\Documents\Koneet\\"
    file_path, file_name = FileOperations.find_path("ACD", dir_path)
    print(file_path)
    print(file_name)
    #shutil.copyfile(file_path, (destination + file_name))



