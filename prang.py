import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import*
from PySide6.QtGui import *

class Simple_drawing_window_prang(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")
        self.cat = QPixmap("images/cat.png")
        

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0)) 
        p.setBrush(QColor(0, 127, 255)) 
        p.drawEllipse(50, 100, 150, 75)  

        p.setBrush(QColor(255, 127, 0))
        p.drawPolygon([QPoint(200, 125), QPoint(250, 100), QPoint(200, 175)])

        p.setBrush(QColor(100, 100, 255)) 
        p.drawPolygon([QPoint(110, 120), QPoint(130, 80), QPoint(150, 120)]) 
        p.drawPolygon([QPoint(120, 170), QPoint(140, 130), QPoint(160, 170)])  

        p.setBrush(QColor(255, 255, 255))  
        p.drawEllipse(110, 130, 20, 20) 
        p.setBrush(QColor(0, 0, 0)) 
        p.drawEllipse(115, 135, 10, 10) 
        
        p.drawPixmap(QRect(200, 100, 320, 320), self.cat)

        p.end()
            
def main():
    app = QApplication(sys.argv)
    
    w = Simple_drawing_window_prang()
    w.show()
    
    return app.exec()
    
if __name__ == "__main__":
    sys.exit(main())