import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblresult = QLabel(self)
        self.lblresult.move(20,20)

        textiput = QLineEdit(self)
        textiput.setEchoMode(3) # 패스워드 모드 1. 글자 안보임 2.검정색 3. 다 보임
        textiput.move(50,40)
        textiput.textChanged[str].connect(self.onChanged) # 글자가 바뀌면

        #필수설정
        self.setWindowTitle('라인에디트')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onChanged(self, text):
        self.lblresult.setText('입력값 : '+ text)
        self.lblresult.adjustSize()

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
