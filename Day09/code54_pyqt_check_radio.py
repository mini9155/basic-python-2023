# 레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class yourapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cbShowTitle = QCheckBox('show Title',self)
        cbShowTitle.move(20,20)
        cbShowTitle.toggle()

        #signal 종류 stateChanged
        #connect() 매개변수 -> 슬롯함수
        cbShowTitle.stateChanged.connect(self.changeTitle)

        cbKorea = QCheckBox('한국',self)
        cbKorea.move(20,60)
        cbKorea.stateChanged.connect(self.checkKorea)

        rbmale = QRadioButton('남성',self)
        rbmale.move(150,20)
        rbmale.setChecked(True)
        rbmale = QRadioButton('여성',self)
        rbmale.move(150,40)
        rbmale.setChecked(True)

        #필수설정
        self.setWindowTitle('절대배치')
        self.setGeometry(300,300,300,300)
        self.show()
        

    def checkKorea(self, state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('나는 한국인')
        else:
            self.setWindowTitle('나는 머지?')    
        
    def changeTitle(self, state):
        if state == Qt.CheckState.Checked: # Qt.checked 도 사용가능
            self.setWindowTitle('체크박스 체크')
        else:
            self.setWindowTitle('체크박스 체크 해제')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yourapp()
    sys.exit(app.exec_())