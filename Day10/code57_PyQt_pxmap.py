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
        pixmap = QPixmap('./Day10/cat.png').scaledToWidth(640).scaledToHeight(320) #scaled 창 크기 조절
        pixmap.size()

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblsize = QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblsize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)

        self.setLayout(vbox)
        #필수설정
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(300, 300, 300, 300)
        self.show()
        
    def setcenter(self):
        qr = self.frameGeometry() # 창 자기 자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터 화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())



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
