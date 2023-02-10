#파일 다이얼로그


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Myapp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.statusBar

        openfile = QAction('open',self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('파일열기')
        openfile.triggered.connect(self.onClicked)

        munubar = self.menuBar()
        munubar.setNativeMenuBar(False)
        fileMenu = munubar.addMenu('&File')
        fileMenu.addAction(openfile)



        #필수설정
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onClicked(self):
        fname = QFileDialog.getOpenFileName(self, '파일열기', './') #파일 하나 생성

        if fname[0]: #파일을 선택했다면
            file = open(fname[0], 'rt', encoding='utf-8')
            with file:
                data = file.read()
                self.textEdit.setText(data)
            
            file.close()
        QMessageBox.about(self,'성공', '로드했습니다') #파일 오픈 시 해당메세지 창을 띄움
    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, '종료', '종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: # QMessageBox가 yes이면 프로그램 종료
            event.accecpt() # 프로그램 종료 - 이벤트를 수락?
        else:
            event.ignore() # 그대로 프로그램 계속..
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
