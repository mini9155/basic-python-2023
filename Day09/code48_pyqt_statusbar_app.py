import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon # PyQt5.QtGui 에 있는 QIcon를 쓴다
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #액션
        actexit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actexit.setShortcut('Ctrl+Q') # 단축기 지정
        actexit.setStatusTip('앱 종료') # 설명
        actexit.triggered.connect(qApp.quit) #이 액션을 실행시키기

        actsave = QAction(QIcon('./Day09/save.png'), 'save', self)
        actsave.setShortcut('Ctrl+S') # 단축기
        actsave.setStatusTip('저장') # 설명
        

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&FIle')
        filemenu.addAction(actexit)

        #툴바
        toolbar = self.addToolBar('MainToolbar') # 툴바 타이틀은 없어도 됨
        toolbar.addAction(actsave) # 툴바에 actsave 추가
        toolbar.addAction(actexit) # 툴바에 actexit 추가


        #상태바
        now = QDate.currentDate() # 현재 일자
        time = QTime.currentTime() # 현재시간
        self.statusBar().showMessage(now.toString('yyyy년-MM월-dd일')+''+time.toString('hh:mm:ss'))
#        self.statusBar().showMessage(time.toString('hh:mm:ss'))
#        self.statusBar().showMessage(now.toString(Qt.ISOdata))
#        self.statusBar().showMessage('statusbar') # statusbar 텍스트 추가
        self.setWindowIcon(QIcon('./Day09/iot.png')) # 아이콘 삽입
        # GUI 화면 설정
        self.setWindowTitle('bar window') # 프로그램 이름 설정
        #아이콘 추가
#        self.setWindowIcon(QIcon('./Day09/iot.png')) # 아이콘 넣기
#       self.move(1920 // 2,1080 //2) # 창 위치 조정, 근데 알아서 정중앙에 나옴
        self.resize(400, 200) # 크기 설정
        self.setcenter()
        self.show() # 핵심!! - 있어야 창이 켜짐
    #화면 중심 셋팅
    def setcenter(self):
        qr = self.frameGeometry() # 창 자기 자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터 화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__': # 만약 이름이 메인이면
    app = QApplication(sys.argv) # QApplication 에 앱을 만들고
    ex = MyApp()
    sys.exit(app.exec_())