# 레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *

class yourapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lable1 = QLabel('Label1', self)
        lable1.move(20, 20)
        lable2 = QLabel('Label2', self)
        lable2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)

        
        
        #필수설정
        self.setWindowTitle('절대배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yourapp()
    sys.exit(app.exec_())