# 레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *

class yourapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1',self) #alt를 누르면 편하게 쓸수 있게 해줌
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2') # alt+2를 누르면 쓰기 편하게 해줌

        btn3 = QPushButton('Button3',self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)


        self.setLayout(vbox)




#필수설정
        self.setWindowTitle('절대배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yourapp()
    sys.exit(app.exec_())