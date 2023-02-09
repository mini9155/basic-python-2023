# 레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *

class yourapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnok = QPushButton('OK')
        btncancle = QPushButton('cancle')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnok)
        hbox.addWidget(btncancle)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)        
        
        self.setLayout(vbox)

        #필수설정
        self.setWindowTitle('절대배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yourapp()
    sys.exit(app.exec_())