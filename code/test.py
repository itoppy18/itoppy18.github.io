import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        hbox = QHBoxLayout(self)
        # QPixmapオブジェクト作成
        pixmap = QPixmap("pirka/background.png")

        # ラベルを作ってその中に画像を置く
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle('Imoyokan')
        self.show()        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
