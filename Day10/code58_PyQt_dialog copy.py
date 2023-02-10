# 이미지 처리 위젯


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btnDlg = QPushButton('Dialog', self) # 버튼을 만든다
        self.btnDlg.move(20, 20) #위치
        self.btnDlg.clicked.connect(self.onClicked) # 클릭하면 온클릭 함수 발동

        self.textinput = QLineEdit(self)
        self.textinput.move(20,50)
        

        #필수설정
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onClicked(self):
        text, ok = QInputDialog.getText(self, '인풋다이얼','이름을 적으세요') # 추가 텍스트창이 나옴 (self, 창제목, 텍스트박스 위 제목)

        if ok:
            self.textinput.setText(text) #  텍스트 박스에 들어간다
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())



















###기본
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

# class Myapp(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         pass

#         #필수설정
#         self.setWindowTitle('라인에디트')
#         self.setGeometry(300, 300, 300, 300)
#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Myapp()
#     sys.exit(app.exec_())
