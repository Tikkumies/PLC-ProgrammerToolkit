from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QPushButton, QGridLayout, QFileDialog, QLineEdit, QComboBox
import shutil
from ...utils.file_operations import FileOperations
from ...utils.handle_json import write_json, read_json

class CopyFiles(QWidget):
    def __init__(self, json_file, diag):
        super().__init__()
        self.json_file = json_file
        self.diag = diag
        self.dict_plc = {"Octopus Siemens": ["path", "file externsion"], "Octopus AB": [r"C:\Users\Mikko\Documents\hakutesti\softakansio", "ACD"], "Compact": ["path", "file externsion"], "Compact AB": ["path", "file externsion"]}
        self.dict_hmi = {"Octoface 2.0": ["path", "file externsion"], "PanelView": ["path", "file externsion"],"Compact 20/TSI": ["path", "file externsion"],
                          "Compact PanelView": "path"}
        self.dict_filmfeeding = {"Octopus Siemens": ["path", "file externsion"], "Octopus AB": ["path", "file externsion"],"Octopus Siemens Twin": ["path", "file externsion"], 
                                 "Octopus AB Twin": ["path", "file externsion"],"Octopus AB": ["path", "file externsion"], "Compact": ["path", "file externsion"], "Compact AB": ["path", "file externsion"]}
        self.dict_vfd ={"1845S": ["path", "file externsion"], "1850T": ["path", "file externsion"]}
        self.destination_folder = r"C:\Users\Mikko\Documents\hakutesti\\"
        self.setObjectName("myParentWidget")
        self.create_widget_objects()
        self.create_layout()


        self.button_copy.clicked.connect(lambda: self.copy_file( [self.check_plc, self.check_hmi, self.check_motec, self.check_vfd],
                                                                [self.combo_plc, self.combo_hmi, self.combo_motec, self.combo_vfd],
                                                                [self.dict_plc, self.dict_hmi, self.dict_filmfeeding, self.dict_vfd]))

    # Creates widget objects
    def create_widget_objects(self):
        self.file_dialog = QFileDialog()
        self.directory_dialog = QFileDialog()

        self.label_create_folder = QLabel("Create project folder")
        self.label_create_folder.setObjectName("DeltaGuiTitle")
        self.label_machine_number_create_folder = QLabel("Machine number")
        self.qline_machine_number_create_folder = QLineEdit("")
        self.qline_machine_number_create_folder.setPlaceholderText("Machine number")
        self.label_path_to_create_folder = QLabel("Path to folder")
        self.qline_path_to_create_folder = QLineEdit(self.destination_folder)
        self.button_create_folder_path = QPushButton("...")
        self.button_create_folder = QPushButton("Create folder")

        self.label_copy_files = QLabel("Copy files")
        self.label_copy_files.setObjectName("DeltaGuiTitle")
        self.label_electrical_drawings = QLabel("Electrical drawings")
        self.qline_electrical_drawings_machine_number = QLineEdit("")
        self.qline_electrical_drawings_machine_number.setPlaceholderText("Machine number")
        self.check_electrical_drawings = QCheckBox(self)

        self.label_plc = QLabel("PLC")
        self.combo_plc = QComboBox(self)
        self.combo_plc.addItems(list(self.dict_plc.keys()))
        self.check_plc = QCheckBox(self)

        self.label_hmi = QLabel("HMI")
        self.combo_hmi = QComboBox(self)
        self.combo_hmi.addItems(list(self.dict_hmi.keys()))
        self.check_hmi = QCheckBox(self)

        self.label_motec = QLabel("Film feeding")
        self.combo_motec = QComboBox(self)
        self.combo_motec.addItems(list(self.dict_filmfeeding.keys()))
        self.check_motec = QCheckBox(self)

        self.label_vfd = QLabel("VFD")
        self.combo_vfd = QComboBox(self)
        self.combo_vfd.addItems(list(self.dict_vfd.keys()))
        self.check_vfd = QCheckBox(self)
        
        self.button_copy = QPushButton("Copy selected files")

        self.placeholder = QLabel("")

    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.label_create_folder, 0, 0)
        self.layout.addWidget(self.label_machine_number_create_folder, 1, 0)
        self.layout.addWidget(self.qline_machine_number_create_folder, 2, 0)
        self.layout.addWidget(self.label_path_to_create_folder, 1, 1)
        self.layout.addWidget(self.qline_path_to_create_folder, 2, 1)
        self.layout.addWidget(self.button_create_folder_path, 2, 2)
        self.layout.addWidget(self.label_copy_files, 3, 0)
        self.layout.addWidget(self.label_electrical_drawings, 4, 0)
        self.layout.addWidget(self.qline_electrical_drawings_machine_number, 4, 1)
        self.layout.addWidget(self.check_electrical_drawings, 4, 2)
       
        self.layout.addWidget(self.label_plc, 5, 0)
        self.layout.addWidget(self.combo_plc, 5, 1)
        self.layout.addWidget(self.check_plc, 5, 2)

        self.layout.addWidget(self.label_hmi, 6, 0)
        self.layout.addWidget(self.combo_hmi, 6, 1)
        self.layout.addWidget(self.check_hmi, 6, 2)

        self.layout.addWidget(self.label_motec, 7, 0)
        self.layout.addWidget(self.combo_motec, 7, 1)
        self.layout.addWidget(self.check_motec, 7, 2)

        self.layout.addWidget(self.label_vfd, 8, 0)
        self.layout.addWidget(self.combo_vfd, 8, 1)
        self.layout.addWidget(self.check_vfd, 8, 2)

        self.layout.addWidget(self.button_copy, 9, 0, 1, 3)
        self.layout.addWidget(self.placeholder, 10, 2)
        self.layout.setRowStretch(10, 5)
        self.setLayout(self.layout)



    def copy_file(self, check_box_list, combo_box_list, data_dictionary_list):
        for (check_box, combo_box, data_dictionary) in zip(check_box_list, combo_box_list, data_dictionary_list):
           if check_box.isChecked():
                list_from_directory = data_dictionary.get(combo_box.currentText())
                dir_path = list_from_directory[0]
                try:
                    file_path, file_name = FileOperations.find_path(list_from_directory[1], dir_path)
                    shutil.copyfile(file_path, (self.destination_folder + file_name))
                except:
                    self.diag.show()

'''
    def update_json_file(self):
        data =  {"IX Developer": self.qline_ix.text(), 
                 "Lenze Engineer" : self.qline_lenze.text(),
                 "WMware" :self.qline_vmware.text(), 
                 "Connect": self.qline_connect.text()}
        write_json(self.json_file, data)

    def read_json(self):
        data = read_json(self.json_file)
        self.qline_ix.setText(data.get("IX Developer"))
        self.qline_lenze.setText(data.get("Lenze Engineer"))
        self.qline_vmware.setText(data.get("WMware"))
        self.qline_connect.setText(data.get("Connect"))
'''
        
