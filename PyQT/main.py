import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtWidgets import QGridLayout

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        
        self.btn = QPushButton('Click me')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        self.btn.setStyleSheet(" font-size: 20px; background-color: lightblue;")

        self.btn.clicked.connect(self.acao)

        self.setCentralWidget(self.cw)

    def acao(self):
        print('Clicked')
        
       
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()