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


        def initUI(self):
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)

        layout = QGridLayout(self.widget)
        layout.addItem(QSpacerItem(0, 300, QSizePolicy.Expanding, QSizePolicy.Minimum), 40, 0)
        layout.addWidget(QPushButton('x', self, clicked=self.accept, objectName='closeButton'), 0, 1)  
        
        
        self.d = QtWidgets.QPushButton(self)
        self.d.setObjectName("closeButton")
        self.d.setGeometry(QtCore.QRect(490, 20, 37, 37))
        self.d.setFont(QtGui.QFont('Tahoma'))
        self.d.setText("-")
        self.d.clicked.connect(self.min)


        self.label_top = QtWidgets.QLabel(self)
        self.label_top.setObjectName("label_top")
        self.label_top.setGeometry(QtCore.QRect(130, 20, 331, 41))   
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top.setText("Youtube Downloader")
        self.label_top.setFont(QtGui.QFont('Tahoma',20))

        self.label_top = QtWidgets.QLabel(self)
        self.label_top.setObjectName("label_top")
        self.label_top.setGeometry(QtCore.QRect(20, 330, 331, 41))  
        self.label_top.setText("Made with love by Bryan Herrera")
        self.label_top.setFont(QtGui.QFont('Tahoma', 10))

        self.button_download = QtWidgets.QPushButton(self)
        self.button_download.setObjectName("button_download")
        self.button_download.setGeometry(QtCore.QRect(240, 190, 111, 51))
        self.button_download.setFont(QtGui.QFont('Tahoma'))
        self.button_download.setText("Download")
        self.button_download.clicked.connect(self.download_button)

        self.check_video = QtWidgets.QCheckBox(self)
        self.check_video.setObjectName("check_video")
        self.check_video.setGeometry(QtCore.QRect(390, 210, 151, 21))
        self.check_video.setFont(QtGui.QFont('Tahoma'))  
        self.check_video.setText("Download Video")

        self.input_url = QtWidgets.QLineEdit(self)
        self.input_url.setObjectName("input_url")
        self.input_url.setGeometry(QtCore.QRect(20, 80, 551, 41))
        self.input_url.setFont(QtGui.QFont('Tahoma'))
        self.input_url.setAlignment(QtCore.Qt.AlignCenter)
        self.input_url.setText("")
        self.input_url.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(238, 104, 55, 1));"
                "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgba(237, 63, 122, 1), stop:1 rgba(238, 104, 55, 1));}");
        pal = self.input_url.palette()
        text_color = QtGui.QColor("white")
        pal.setColor(QtGui.QPalette.PlaceholderText, text_color)
        self.input_url.setPalette(pal)
        self.input_url.setPlaceholderText("Enter URL Here...")

        self.button_set = QtWidgets.QPushButton(self)
        self.button_set.setObjectName("button_set")
        self.button_set.setGeometry(QtCore.QRect(500, 130, 71, 41))
        self.button_set.setFont(QtGui.QFont('Tahoma'))
        self.button_set.setText("Set")
        self.button_set.clicked.connect(self.set_button)

        self.input_path = QtWidgets.QLineEdit(self)
        self.input_path.setObjectName("input_path")
        self.input_path.setGeometry(QtCore.QRect(20, 130, 471, 41))
        self.input_path.setFont(QtGui.QFont('Tahoma'))
        self.input_path.setAlignment(QtCore.Qt.AlignCenter)
        self.input_path.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(238, 104, 55, 1));"
                "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgba(237, 63, 122, 1), stop:1 rgba(238, 104, 55, 1));}");
        pall = self.input_path.palette()
        text_colorr = QtGui.QColor("white")
        pall.setColor(QtGui.QPalette.PlaceholderText, text_colorr)
        self.input_path.setPalette(pall)
        self.input_path.setPlaceholderText(self.std_download_path)


        self.radio_single = QtWidgets.QRadioButton(self)
        self.radio_single.setObjectName("radio_single")
        self.radio_single.setGeometry(QtCore.QRect(390, 180, 81, 21))
        self.radio_single.setFont(QtGui.QFont('Tahoma'))
        self.radio_single.setText("Single")
        self.radio_single.setChecked(True)

        self.radio_playlist = QtWidgets.QRadioButton(self)
        self.radio_playlist.setObjectName("radio_playlist")
        self.radio_playlist.setGeometry(QtCore.QRect(470, 180, 81, 21))
        self.radio_playlist.setFont(QtGui.QFont('Tahoma'))
        self.radio_playlist.setText("Playlist")

        self.label_done = QtWidgets.QLabel(self)
        self.label_done.setObjectName("label_done")
        self.label_done.setGeometry(QtCore.QRect(210, 260, 171, 31))
        self.label_done.setFont(QtGui.QFont('Tahoma'))
        self.label_done.setAlignment(QtCore.Qt.AlignCenter)
        self.label_done.setText("")

        self.combo_quality = QtWidgets.QComboBox(self)
        self.combo_quality.addItem("")
        self.combo_quality.addItem("")
        self.combo_quality.addItem("")
        self.combo_quality.setObjectName("combo_quality")
        self.combo_quality.setGeometry(QtCore.QRect(90, 210, 69, 22))
        self.combo_quality.setFont(QtGui.QFont('Tahoma'))
        self.combo_quality.setItemText(0, "Best")
        self.combo_quality.setItemText(1, "Semi")
        self.combo_quality.setItemText(2, "Worst")

        self.label_quality = QtWidgets.QLabel(self)
        self.label_quality.setObjectName("label_quality")
        self.label_quality.setGeometry(QtCore.QRect(50, 180, 151, 21))
        self.label_quality.setFont(QtGui.QFont('Tahoma'))
        self.label_quality.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quality.setText("Download Quality:")


    

