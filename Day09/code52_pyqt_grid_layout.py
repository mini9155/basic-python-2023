# 레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *

class yourapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('TItle'),0,0) #row, col = 0,0
        grid.addWidget(QLabel('Author'),1,0)
        grid.addWidget(QLabel('Review'),2,0)

        grid.addWidget(QLineEdit(),0,1) # 0행 1렬
        grid.addWidget(QLineEdit(),1,1)
        grid.addWidget(QTextEdit(),2,1)


        btnok = QPushButton('OK')
        btncancle = QPushButton('cancle')

        grid.addWidget(btnok, 3, 1)
        grid.addWidget(btncancle, 3, 2)


        #필수설정
        self.setWindowTitle('절대배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yourapp()
    sys.exit(app.exec_())