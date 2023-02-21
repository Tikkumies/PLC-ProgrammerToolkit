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
        font-size: 16px;
        color: #FFFFFF;
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:0,
                                        stop:0 #404040 , stop:1 #404040);
        spacing: 3px;
    }

    QMenuBar::item {
        padding: 1px 4px;
        background-color: #404040;
        border-radius: 4px;
    }

    QMenuBar::item:selected {
        background-color: #181818;
    }

    QMenuBar::item:pressed {
        background-color: #B2B2B2;
    }

    QMenu{
        background-color: #404040;
        spacing: 3px;
        color: #FFFFFF

    }
    QMenu::item{
        background-color: transparent;
        font-size: 16px;
        padding: 6px;

    }

    QMenu::item::selected{
        background-color: #181818;
        color: #FFFFFF;
        font-size: 16px;
    }
    """
