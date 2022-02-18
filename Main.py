import os
import sys
from os import path
import subprocess

class MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)
        self.setStyleSheet("""
        #Custom_Widget {
            background: #2B1046;
            border: 3px solid rgba(237, 63, 122, 1);
            color: #fff;
            border-radius: 15px;                  
        } 
        QLabel {
            color: #fff;
        }
        QPushButton {
            background: #6C31A5;
            border-radius: 15px;
            border: 0px solid transparent;
        }
        QPushButton:hover {
            background: rgba(237, 63, 122, 1);
        }
        QRadioButton {
            color: #fff;
        }
        QCheckBox {
            color: #fff;
        }
        QLineEdit {
            border: 0px solid transparent;
            border-radius: 15px;
            color: #ffffff;
        }
        
        #closeButton {
            background: rgba(237, 63, 122, 1);
            min-width: 36px;
            min-height: 36px;
            border-radius: 10px;
        }
        #closeButton:hover {
            color: #ccc;
            background: red;
        }
        """)
        
        self.setGeometry(200, 200, 592, 316)
        self.setWindowTitle("Youtube Downloader | Miguel Herrera")
        self.font = QtGui.QFont()
        self.std_download_path = str(os.path.join(os.path.expanduser("~"), "Downloads"))
        self.label_1 = QLabel("new border ", self)
        self.setMaximumWidth(592)
        self.setMaximumHeight(200)
        
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        
        self.setFixedSize(QSize(592, 316))
        self.setMaximumWidth(self.width())
        self.setMaximumHeight(self.height())

        self.initUI()

    

