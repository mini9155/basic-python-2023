import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon # PyQt5.QtGui 에 있는 QIcon를 쓴다

class MyApp(QWidget): # QWidget을 상속 받아서 쓸꺼야
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('simple Windows') # 프로그램 이름 설정
        #아이콘 추가
        self.setWindowIcon(QIcon('./Day09/iot.png')) # 아이콘 넣기
#       self.move(1920 // 2,1080 //2) # 창 위치 조정, 근데 알아서 정중앙에 나옴
        self.resize(400, 200) # 크기 설정
        self.show() # 핵심!! - 있어야 창이 켜짐
        
if __name__ == '__main__': # 만약 이름이 메인이면
    app = QApplication(sys.argv) # QApplication 에 앱을 만들고
    ex = MyApp()
    sys.exit(app.exec_())