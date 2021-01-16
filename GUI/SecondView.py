from GUI.styles import *
from GUI.Frames import *

from PyQt5 import QtCore, QtGui


class SecondView(QWidget):
    def __init__(self, width=800, height=480):
        super().__init__()

        self.setFixedSize(width, height)
        self.font = QtGui.QFont('Digital-7 Mono')
        self.font2 = QtGui.QFont('LEMON MILK')
        
        self.gear_LCD = QLabel(self)
        self.init_gear_LCD()

        self.rpm = LCD_Display(self, self.font)    
        self.init_rpm()

        self.speed = LCD_Display(self, self.font)        
        self.init_speed()

        self.warning_list = []
        self.warning = Warning(self, self.font2)
        self.init_warning()

        self.info1 = Info_type_1(self, self.font2)
        self.init_info1()

        self.info2 = Info_type_2(self, self.font2)
        self.init_info2()        
        
        self.info3 = Info_type_3(self, "Info1", self.font2)
        self.info4 = Info_type_3(self, "Info2", self.font2)
        self.info5 = Info_type_3(self, "Info3", self.font2)
        self.init_info3()
        


    def init_gear_LCD(self):
        self.gear_LCD.setFixedSize(GEAR_WIDTH, GEAR_HEIGHT)
        self.gear_LCD.move((int(self.width()) - GEAR_WIDTH) / 2 , GEAR_HEIGHT)
        self.gear_LCD.setFont(self.font)
        self.gear_LCD.setAlignment(QtCore.Qt.AlignCenter)
        self.gear_LCD.setStyleSheet(INFO_GEAR)
        self.gear_LCD.setText('0')


    def init_rpm(self):
        self.rpm.setFixedSize(int(self.width() / 2), GEAR_HEIGHT)
        self.rpm.move(0, 0)       
       
        self.rpm.value.setFixedSize(GEAR_WIDTH * 3.1, GEAR_HEIGHT * 0.75)       
        self.rpm.value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.rpm.value.setText('22000')
        self.rpm.value.setStyleSheet(INFO_RPM_2)
        
        self.rpm.unit.setFixedWidth(GEAR_WIDTH * 3)
        self.rpm.unit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.rpm.unit.setStyleSheet(UNIT_RPM)
        self.rpm.unit.setText('RPM')


    def init_speed(self):
        self.speed.setFixedSize(int(self.width() / 2), GEAR_HEIGHT)
        self.speed.move(int(self.width() / 2), 0)
        
        self.speed.value.setFixedSize(int(GEAR_WIDTH * 1.85), GEAR_HEIGHT * 0.75)       
        self.speed.value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.speed.value.setText('220')
        self.speed.value.setStyleSheet(INFO_RPM_2)
        
        self.speed.unit.setFixedWidth(int(GEAR_WIDTH * 1.85))
        self.speed.unit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.speed.unit.setStyleSheet(UNIT_RPM)
        self.speed.unit.setText('KMPH')


    def init_info1(self):
        self.info1.setFixedSize(int((self.width() - GEAR_WIDTH) / 2), int((self.height() - GEAR_HEIGHT) / 2))
        self.info1.move(0, GEAR_HEIGHT)
 
        self.info1.info1.value.setText('0')
        self.info1.info2.value.setText('0')
        self.info1.info3.value.setText('0')
        self.info1.info4.value.setText('0')

        
    def init_info2(self):
        self.info2.setFixedSize(int((self.width() - GEAR_WIDTH) / 2), int((self.height() - GEAR_HEIGHT) / 2))
        self.info2.move(int((self.width() + GEAR_WIDTH) / 2), GEAR_HEIGHT)
        self.info2.info1.value.setText('5')
        self.info2.info2.value.setText('0')
        self.info2.info3.value.setText('0')
        self.info2.info4.value.setText('0')


    def init_info3(self):
        self.info3.setFixedSize(int(self.width() / 6), int((self.height() - GEAR_HEIGHT) / 2))
        self.info3.move(0, GEAR_HEIGHT * 2)
        self.info4.setFixedSize(int(self.width() / 6), int((self.height() - GEAR_HEIGHT) / 2))
        self.info4.move(int(self.width() / 6), GEAR_HEIGHT * 2)
        self.info5.setFixedSize(int((self.width()) / 6), int((self.height() - GEAR_HEIGHT) / 2))
        self.info5.move(int(self.width() / 3), GEAR_HEIGHT * 2)
        
        self.info3.value.setText('0')
        self.info4.value.setText('0')
        self.info5.value.setText('10')


    def init_warning(self):
        self.warning.setFixedSize(int(self.width()  / 2), int((self.height() - GEAR_HEIGHT) / 2))
        self.warning.move(int(self.width()  / 2), GEAR_HEIGHT + int((self.height() - GEAR_HEIGHT) / 2))


class Info_type_1(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent)
        layout1 = QtWidgets.QVBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)

        self.info1 = Wid(parent, "Info1", font)
        self.info2 = Wid(parent, "Info2", font)
        self.info3 = Wid(parent, "Info3", font)
        self.info4 = Wid(parent, "Info4", font)
        
        layout1.addWidget(self.info1)
        layout1.addWidget(self.info2)
        layout1.addWidget(self.info3)
        layout1.addWidget(self.info4)
        
        self.setLayout(layout1)
        self.setStyleSheet(QFRAME_STYLE)


class Info_type_2(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent)
        layout1 = QtWidgets.QVBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)

        self.info1 = Wid(parent, "Info1", font)
        self.info2 = Wid(parent, "Info2", font)
        self.info3 = Wid(parent, "Info3", font)
        self.info4 = Wid(parent, "Info4", font)
        
        layout1.addWidget(self.info1)
        layout1.addWidget(self.info2)
        layout1.addWidget(self.info3)
        layout1.addWidget(self.info4)
        
        self.setLayout(layout1)
        self.setStyleSheet(QFRAME_STYLE)


class Info_type_3(QFrame):
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
        self.value.setStyleSheet(INFO_LABEL_VALUE_2)
        self.value.setAlignment(QtCore.Qt.AlignCenter)
        self.value.setFont(font)

        layout.addWidget(self.value)
        layout.addWidget(info)
        self.setLayout(layout)
        self.setStyleSheet(QFRAME_STYLE)