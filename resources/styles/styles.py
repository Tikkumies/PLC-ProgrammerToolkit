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

    QLabel#DeltaGuiTitle {
        font-size: 20px;
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
        padding: 3px;
        background-color: transparent;
        spacing: 3px;
    }

    QMenuBar::item {
        padding: 1px 4px;
        background-color: #404040;
        border-radius: 4px;
        padding: 7px
    }

    QMenuBar::item:selected {
        background-color: #282828;
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
        width: 150px;

    }

    QMenu::item::selected{
        background-color: #181818;
        color: #FFFFFF;
        font-size: 16px;
    }

    QCheckBox {

    }

    QCheckBox::indicator {
        width: 35px;
        height: 35px;
    }

    QCheckBox::indicator:unchecked {
        image: url(resources/images/uncheck.png);
    }

    QCheckBox::indicator:checked {
    image: url(resources/images/checked.png);
    }

    """
