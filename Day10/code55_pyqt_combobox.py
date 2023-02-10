# 레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class yourapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): #self. 을 쓰면 내 클래스에 있는 함수로 만듬(전역변수)
        self.lblOption = QLabel('선택값 : ', self)
        self.lblOption.move(20, 20) # 위치 조정

        cboption = QComboBox(self)
        cboption.addItem('option1') #items는 여러개
        cboption.addItem('option2') # 콤보박스를 만듬
        cboption.addItem('option3')
        cboption.addItem('option4')
        cboption.addItem('option5')
        cboption.move(20,40) # 위치
        cboption.activated[str].connect(self.onActivated)
        #필수설정
        self.setWindowTitle('콥보박스') # 타이틀바 이름
        self.setGeometry(300,300,300,300)
        self.show()
        
    def onActivated(self, text):
        self.lblOption.setText('선택값 :' + text)
        self.lblOption.adjustSize() #글자수만큼 라벨 넓이 조절

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