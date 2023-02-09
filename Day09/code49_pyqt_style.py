#스타일
import sys
from PyQt5.QtWidgets import *

class Myapp(QWidget): 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #스타일 설정
        lbl_red = QLabel('Red')
        lbl_red.setStyleSheet('color:red;''border-style:solid;''border-width: 5px;''border-color:#FA8072;''border-radius:10px;')
        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet('color:red;''border-style:dashed;''border-width: 5px;''border-color:#7FFFD4;''border-radius:10px;')


        # QV 세로 QH 가로
        vbox = QVBoxLayout()# 세로 구분 짓는 레이아웃
        vbox.addWidget(lbl_red) #위젯 추가
        vbox.addWidget(lbl_green) #위젯 추가

        self.setLayout(vbox) # 전체 레이아웃에 vbox를 추가
        self.setWindowTitle('스타일지정')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())