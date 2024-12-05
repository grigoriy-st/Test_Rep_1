import sys
from random import randint


import random
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QWidget,
)
from PyQt6.QtGui import QPainter, QColor


class Main_Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        uic.loadUi("dialog.ui", self)
        self.circles = []
        self.button.clicked.connect(self.add_circle)


    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("yellow"))
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main_Window()
    ui.show()
    sys.exit(app.exec())
