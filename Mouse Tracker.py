import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Task Week 3 - (F1D022095 - Rizky Maulana Ramdhani)")
        self.setGeometry(100, 100, 400, 300)
        
        self.label = QLabel("Gerakkan mouse pada window", self)
        self.label.setGeometry(50, 50, 200, 50)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
        
        self.canMove = True
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.enableMovement)
        
        self.show()
    
    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        self.label.setText(f"Mouse Position: (x : {x}, y : {y})")
        if self.canMove and self.label.geometry().contains(event.pos()):
            self.moveLabel()
            self.canMove = False
            self.timer.start(500)
        
    def moveLabel(self):
        new_x = random.randint(0, self.width() - self.label.width())
        new_y = random.randint(0, self.height() - self.label.height())
        self.label.move(new_x, new_y)

    def enableMovement(self):
        self.canMove = True
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    sys.exit(app.exec_())