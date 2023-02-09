import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn  = QPushButton('Quit', self) # 버튼 안에 텍스트 값
        btn.move(320, 170) # 버튼 위치 조정
        btn.resize(btn.sizeHint())
        #버튼 툴팁
        btn.setToolTip('이거 누르면 그냥 꺼져요. <b>조심</b>하세요') # quit 버튼 누르기 전에 메시지창
        btn.clicked.connect(QCoreApplication.instance().quit) # quit 누르면 종료되게 해줌
    

        self.setWindowIcon(QIcon('./Day09/iot.png')) # 메인바 아이콘 위치
        self.setWindowTitle('Quit button')
        self.setGeometry(900,200,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())