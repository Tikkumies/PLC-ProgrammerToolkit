GLOBAL_STYLE = """
    QPushButton {
        font-size: 16px;
        text-align:center;
        border-radius: 5;
        border: 1px;
        background-color: #404040;
        color: #FFFFFF;
        padding: 5px;
        }

    QPushButton:pressed {
        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #B2B2B2, stop: 1 #B2B2B2);
    }

        QPushButton:hover:!pressed
    {
    background-color: #181818; 
    }

    QLabel {
        font-size: 16px;
        border: 1px;
        background-color: #121212;
        color: #FFFFFF;
        }
        
    QLineEdit{
        font-size: 16px;
        border-radius: 5;
        border: 1px;
        background-color: #404040;
        color: #FFFFFF;
        padding: 5px;
        selection-background-color: #121212;

    }
    QComboBox{
        font-size: 16px;
        border-radius: 5;
        border: 1px;
        background-color: #404040;
        color: #FFFFFF;
        padding: 5px;
        }

    QComboBox QAbstractItemView {
        background-color: #404040;
        color: #FFFFFF;
        selection-background-color: #282828;
    }

    QWidget#myParentWidget{
        background-color: #121212;
    }
    QMenuBar {
        background-color: #404040;
        color: #FFFFFF;
        font-size: 16px;
    }
    """
