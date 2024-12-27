import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window_kp(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")
        self.fish = QPixmap("images/fish.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(70, 100),
            QPoint(100, 110),
            QPoint(130, 100),
            QPoint(100, 150),
            QPoint(80, 300),
            QPoint(59, 100)
        ])

        p.drawPixmap(QRect(200, 100, 320, 320), self.fish)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window_kp()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
