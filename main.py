import sys
from random import randint


import random
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QWidget,
)
from PyQt6.QtGui import QPainter, QColor
from UI import Ui_Dialog

class Main_Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.circles = []
        self.ui.button.clicked.connect(self.add_circle)


    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter, color) in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main_Window()
    ui.show()
    sys.exit(app.exec())
