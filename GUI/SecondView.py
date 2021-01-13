try:
    from GUI.styles import *
except:
    from Dashboard.GUI.styles import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber, QLabel, QProgressBar, QWidget, QFrame


class SecondView(QWidget):
    def __init__(self, main_window):
        super().__init__(parent=main_window)

        self.setFixedSize(main_window.width(), main_window.height())
        self.font = QtGui.QFont('Digital-7 Mono')
        self.font2 = QtGui.QFont('LEMON MILK')
        self.gear_LCD = QLabel(main_window)
        self.init_gear_LCD()


    def init_gear_LCD(self):
        self.gear_LCD.setFixedSize(GEAR_SIZE * 0.65, GEAR_SIZE)
        self.gear_LCD.move((int(self.width()) - GEAR_SIZE * 0.65) / 2 , 0)
        self.gear_LCD.setFont(self.font)
        self.gear_LCD.setAlignment(QtCore.Qt.AlignCenter)
        self.gear_LCD.setStyleSheet(INFO_GEAR)
        self.gear_LCD.setText('0')