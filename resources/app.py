from resources.mainwindow import *


def main():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        os.chdir(sys._MEIPASS)
    app = QApplication(sys.argv)
    dialog = Dialog()
    ip_window = Window(dialog)
    test_window = TestWindow()
    main_window = MainWindow(ip_window, test_window)
    main_window.show()
    ip_window.setStyleSheet(styles.GLOBAL_STYLE)
    test_window.setStyleSheet(styles.GLOBAL_STYLE)
    main_window.setStyleSheet(styles.GLOBAL_STYLE)
    sys.exit(app.exec_())
