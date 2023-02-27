from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QPushButton, QGridLayout, QFileDialog, QLineEdit
import shutil
from ...utils.file_operations import FileOperations
from ...utils.handle_json import write_json, read_json

class CopyFiles(QWidget):
    def __init__(self, json_file):
        super().__init__()
        #self.diag = diag
        self.json_file = json_file
        self.setObjectName("myParentWidget")
        self.create_widget_objects()
        self.create_layout()

        self.button_electrical_src.clicked.connect(lambda: self.open_file_dialog(self.qline_electrical_src))
        self.button_electrical_dest.clicked.connect(lambda: self.open_directory_dialog(self.qline_electrical_dest))
        self.button_copy.clicked.connect(lambda: self.copy_file())

    # Creates widget objects
    def create_widget_objects(self):
        self.label_title = QLabel("Copy files")
        self.label_title.setObjectName("DeltaGuiTitle")
        self.file_dialog = QFileDialog()
        self.directory_dialog = QFileDialog()

        self.Label_electrical = QLabel("Elec drawings")
        self.check_electrical = QCheckBox()
        self.button_electrical_src = QPushButton("...")
        self.qline_electrical_src = QLineEdit("")
        self.button_electrical_dest = QPushButton("...")
        self.qline_electrical_dest = QLineEdit("")


        self.label_placeholder = QLabel("")

        self.button_copy = QPushButton("Copy")

    def create_layout(self):
        self.layout = QGridLayout()

        self.layout.addWidget(self.label_title, 0, 0)
        self.layout.addWidget(self.Label_electrical, 1, 0)
        #self.layout.addWidget(self.check_electrical, 1, 1)
        self.layout.addWidget(self.qline_electrical_src, 1, 2)
        #self.layout.addWidget(self.button_electrical_src, 1, 3)
        self.layout.addWidget(self.qline_electrical_dest, 2, 2)
        self.layout.addWidget(self.button_electrical_dest, 2, 3)
        self.layout.addWidget(self.button_copy, 3, 1, 1, 2)

        self.layout.addWidget(self.label_placeholder, 7, 0)
        self.layout.setRowStretch(8, 5)

        self.setLayout(self.layout)

    def open_file_dialog(self, line_edit_text):
        line_edit_text.setText(self.file_dialog.getOpenFileName(self, "Select file")[0])

    def open_directory_dialog(self, line_edit_text):
        line_edit_text.setText(self.directory_dialog.getExistingDirectory(self, "Select directory"))

    def copy_file(self):
        dir_path = r"C:\Users\Mikko\Documents\hakutesti\ITW-haloila"
        destination = r"C:\Users\Mikko\Documents\hakutesti\\"
        file_path = FileOperations.find_path(self.qline_electrical_src.text(), dir_path)
        shutil.copyfile(file_path, (destination + self.qline_electrical_src.text() + ".pdf"))

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
        
