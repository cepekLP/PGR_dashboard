import logging

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QFrame

from GUI.styles import *


#wyswietalcz rpm / kmph
class LCD_Display(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.value = QLabel()
        self.unit = QLabel()

        self.value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.value.setFont(font)
        self.unit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.unit.setFont(font)
        
        layout.addWidget(self.value, 0, QtCore.Qt.AlignHCenter)       
        layout.addWidget(self.unit, 0, QtCore.Qt.AlignHCenter)
        self.setLayout(layout)
        self.setStyleSheet(QFRAME_STYLE)



#wyświetlacz ostrzeżeń
class Warning(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent)
        layout = QtWidgets.QVBoxLayout()
        
        self.tekst = QLabel()
        self.tekst.setStyleSheet(INFO_LABEL_VALUE)
        self.tekst.setAlignment(QtCore.Qt.AlignCenter)
        self.tekst.setWordWrap(True)
        self.tekst.setFont(font)
        layout.addWidget(self.tekst)
        
        self.setLayout(layout)
        self.setStyleSheet(WARNING_QFRAME_STYLE % (0, 0, 0))

        self.list = []
        
    
    #aktualizacja wyświetlacza
    def update(self):        
        if len(self.list) == 0:
            self.tekst.setText("")
            self.setStyleSheet(WARNING_QFRAME_STYLE % (0, 0, 0))
        else:
            if self.list[0][0] == 0:
                self.setStyleSheet(WARNING_QFRAME_STYLE % (255, 0, 0))
            elif self.list[0][0] == 1:
                self.setStyleSheet(WARNING_QFRAME_STYLE % (255, 128, 0))
            elif self.list[0][0] == 2:
                self.setStyleSheet(WARNING_QFRAME_STYLE % (0, 192, 0))
            
            self.tekst.setText(self.list[0][1])
        
    
    #dodanie ostrzeżenia do listy
    def add(self, list):       
        if list[0] == "error":
            self.list.append([0, list[1]])
        elif list[0] == "warning":
             self.list.append([1, list[1]])
        elif list[0] == "info":
             self.list.append([2, list[1]])

        self.list.sort()
        self.update()


    #usuniecie 1 ostrzeżenia z listy
    def delete(self):
        if len(self.list) > 0:
            del self.list[0]
            self.update()            
        else: 
            pass



#etykieta i wartość
class Wid(QWidget):
    def __init__(self, parent, tekst, font, info_width=None):
        super().__init__(parent = parent)
        
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        info = QLabel(tekst)
        info.setStyleSheet(INFO_LABEL_TEXT)
        info.setAlignment(QtCore.Qt.AlignCenter)
        info.setFont(font)
        info.setWordWrap(True)
        if info_width != None:
            info.setFixedWidth(info_width)

        self.value = QLabel()
        self.value.setStyleSheet(INFO_LABEL_VALUE)
        self.value.setAlignment(QtCore.Qt.AlignCenter)
        self.value.setFont(font)

        layout.addWidget(info)
        layout.addWidget(self.value)
        self.setLayout(layout)



#wartość nad etykietą
class Wid2(QFrame):
    def __init__(self, parent, tekst, font):
        super().__init__(parent = parent)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        info = QLabel(tekst)
        info.setStyleSheet(INFO_LABEL_TEXT)        
        info.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        info.setFont(font)

        self.value = QLabel()
        self.value.setStyleSheet(INFO_LABEL_VALUE_VERTICAL)
        self.value.setAlignment(QtCore.Qt.AlignCenter)
        self.value.setFont(font)

        layout.addWidget(self.value)
        layout.addWidget(info)
        self.setLayout(layout)
        self.setStyleSheet(QFRAME_STYLE)