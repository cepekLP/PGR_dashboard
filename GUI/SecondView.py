try:
    from GUI.styles import *
except:
    from Dashboard.GUI.styles import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber, QLabel, QProgressBar, QWidget, QFrame


class SecondView(QWidget):
    def __init__(self, width=800, height=480):
        super().__init__()

        self.setFixedSize(width, height)
        self.font = QtGui.QFont('Digital-7 Mono')
        self.font2 = QtGui.QFont('LEMON MILK')
        self.gear_LCD = QLabel(self)
        self.init_gear_LCD()


    def init_gear_LCD(self):
        self.gear_LCD.setFixedSize(GEAR_WIDTH, GEAR_HEIGHT)
        self.gear_LCD.move((int(self.width()) - GEAR_WIDTH) / 2 , 0)
        self.gear_LCD.setFont(self.font)
        self.gear_LCD.setAlignment(QtCore.Qt.AlignCenter)
        self.gear_LCD.setStyleSheet(INFO_GEAR)
        self.gear_LCD.setText('0')