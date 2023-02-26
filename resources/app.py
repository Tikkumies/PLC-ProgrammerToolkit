from resources.mainwindow import *


def main():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        os.chdir(sys._MEIPASS)
    app = QApplication(sys.argv)
    dialog_ip_changer = Dialog("Incorrect network settings", "resources/images/ip.PNG",
                               "Incorrect IP address, network mask or default gateway")
    dialog_delta = Dialog("Values missing", "resources/images/ip.PNG",
                          "Values missing from input fields. Check values and try again.")
    dialog_capacity = Dialog("Values missing", "resources/images/ip.PNG",
                        "Values missing from input fields. Check values and try again.")
    ip_window = Window(dialog_ip_changer)
    delta_window = DeltaWindow(dialog_delta)
    capacity_window = CapacityWindow(dialog_capacity)
    open_programs_window = OpenPrograms()
    main_window = MainWindow(ip_window, delta_window,
                             capacity_window, open_programs_window, "resources/images/ip.PNG")
    main_window.show()
    ip_window.setStyleSheet(styles.GLOBAL_STYLE)
    delta_window.setStyleSheet(styles.GLOBAL_STYLE)
    main_window.setStyleSheet(styles.GLOBAL_STYLE)
    dialog_delta.setStyleSheet(styles.GLOBAL_STYLE)
    dialog_ip_changer.setStyleSheet(styles.GLOBAL_STYLE)
    dialog_capacity.setStyleSheet(styles.GLOBAL_STYLE)
    sys.exit(app.exec_())
