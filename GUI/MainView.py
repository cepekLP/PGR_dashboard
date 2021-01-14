try:
    from GUI.styles import *
except:
    from Dashboard.GUI.styles import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber, QLabel, QProgressBar, QWidget, QFrame


class MainView(QWidget):
    def __init__(self, width=800, height=480):
        super().__init__()

        self.setFixedSize(width, height)
        self.font = QtGui.QFont('Digital-7 Mono')
        self.font2 = QtGui.QFont('LEMON MILK')

        self.gear_LCD = QLabel(self)
        self.init_gear_LCD()
       
        self.rpm = Wid2(self, self.font)    
        self.init_rpm()

        self.speed = Wid2(self, self.font)        
        self.init_speed()

        self.info = Info(self, self.font2)
        self.init_info()

        #self.info2 = Info2(main_window, self.font2)
        #self.init_info2()
        
        self.info2 = Info3(self,"Info1", self.font2)
        self.info3 = Info3(self,"Info2", self.font2)
        self.init_info3()

        self.warning = Warning(self, self.font2)
        self.init_warning()


    def init_gear_LCD(self):
        self.gear_LCD.setFixedSize(GEAR_SIZE * 0.65, GEAR_SIZE)
        self.gear_LCD.move((int(self.width()) - GEAR_SIZE * 0.65) / 2 , 0)
        self.gear_LCD.setFont(self.font)
        self.gear_LCD.setAlignment(QtCore.Qt.AlignCenter)
        self.gear_LCD.setStyleSheet(INFO_GEAR)
        self.gear_LCD.setText('n')


    def init_rpm(self):
        self.rpm.move(int((self.width() - GEAR_SIZE * 0.65) / 2) - self.rpm.width(), 0)       
       
        self.rpm.value.setFixedSize(GEAR_SIZE * 1.5, GEAR_SIZE * 0.7)       
        self.rpm.value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.rpm.value.setText('12000')
        self.rpm.value.setStyleSheet(INFO_RPM)
        
        self.rpm.unit.setFixedWidth(GEAR_SIZE * 1.5)
        self.rpm.unit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.rpm.unit.setStyleSheet(UNIT_RPM)
        self.rpm.unit.setText('RPM')


    def init_speed(self):
        self.speed.move(int((self.width() + GEAR_SIZE * 0.65) / 2), 0)
        
        self.speed.value.setFixedSize(GEAR_SIZE , GEAR_SIZE * 0.7)       
        self.speed.value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.speed.value.setText('120')
        self.speed.value.setStyleSheet(INFO_RPM)
        
        self.speed.unit.setFixedWidth(GEAR_SIZE)
        self.speed.unit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.speed.unit.setStyleSheet(UNIT_RPM)
        self.speed.unit.setText('KMPH')


    def init_info(self):
        self.info.setFixedSize(int(self.width() / 2), self.height() - GEAR_SIZE)
        self.info.move(0, GEAR_SIZE)
        self.info.water_temp.value.setText('  100°C')
        self.info.oil_temp.value.setText('  100°C')
        self.info.break_balance.value.setText('0')
        self.info.TCS.value.setText('0')
        self.info.info5.value.setText('0')
        self.info.info6.value.setText('0')
        self.info.info7.value.setText('0')

        
    def init_info2(self):
        self.info2.setFixedSize(int(self.width() / 2), int((self.height() - GEAR_SIZE) / 2))
        self.info2.move(int(self.width() / 2), GEAR_SIZE)
        self.info2.info1.value.setText('0')
        self.info2.info2.value.setText('0')
        self.info2.info3.value.setText('0')
        self.info2.info4.value.setText('0')


    def init_info3(self):
        self.info2.setFixedSize(int(self.width() / 4), int((self.height() - GEAR_SIZE) / 2))
        self.info2.move(int(self.width() / 2), GEAR_SIZE)
        self.info3.setFixedSize(int(self.width() / 4), int((self.height() - GEAR_SIZE) / 2))
        self.info3.move(int(self.width() *0.75), GEAR_SIZE)
        
        self.info2.value.setText('10')
        self.info3.value.setText('10')

    
    def init_warning(self):
        self.warning.setFixedSize(int(self.width() / 2), int((self.height() - GEAR_SIZE) / 2))
        self.warning.move(int(self.width() / 2), GEAR_SIZE + int((self.height() - GEAR_SIZE) / 2))


    def update(self, display_info):
        self.gear_LCD.setText(str(display_info.gear))        
        self.rpm.value.setText(str(display_info.rpm))  
        self.speed.value.setText(str(display_info.speed))
        self.info.water_temp.value.setText("{}°C".format(display_info.water_temp))
        self.info.oil_temp.value.setText("{}°C".format(display_info.oil_temp))
        self.info.break_balance.value.setText(str(display_info.break_balance))
        self.info.TCS.value.setText(str(display_info.race_tcs_mode))     


    def update_warning(self, type, text_info):        
        if type == "none":
            self.warning.tekst.setText("")
            self.warning.setStyleSheet(WARNING_QFRAME_STYLE % (0, 0, 0))
        elif type == "info":
            self.warning.tekst.setText(text_info)
            self.warning.setStyleSheet(WARNING_QFRAME_STYLE % (0, 192, 0))
        elif type == "warning":
            self.warning.tekst.setText(text_info)
            self.warning.setStyleSheet(WARNING_QFRAME_STYLE % (255, 128, 0))
        elif type == "error":
            self.warning.tekst.setText(text_info)
            self.warning.setStyleSheet(WARNING_QFRAME_STYLE % (255, 0, 0))


    


class Wid2(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent) 
        self.setFixedSize(int((parent.width() - GEAR_SIZE * 0.65) / 2), GEAR_SIZE)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.value = QLabel()
        self.unit = QLabel()

        self.value.setFont(font)
        self.unit.setFont(font)
        
        layout.addWidget(self.value, 0, QtCore.Qt.AlignHCenter)       
        layout.addWidget(self.unit, 0, QtCore.Qt.AlignHCenter)
        self.setLayout(layout)
        self.setStyleSheet(QFRAME_STYLE)


class Info(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent)
        layout1 = QtWidgets.QVBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)

        self.water_temp = Wid(parent, "Water temp", font)
        self.oil_temp = Wid(parent, "Oil temp", font)
        self.break_balance = Wid(parent, "Break balance", font)
        self.TCS = Wid(parent, "TCS", font)
        self.info5 = Wid(parent, "info5", font)
        self.info6 = Wid(parent, "info6", font)
        self.info7 = Wid(parent, "info7", font)

        layout1.addWidget(self.water_temp)
        layout1.addWidget(self.oil_temp)
        layout1.addWidget(self.break_balance)
        layout1.addWidget(self.TCS)
        layout1.addWidget(self.info5)
        layout1.addWidget(self.info6)
        layout1.addWidget(self.info7)
        
        self.setLayout(layout1)
        self.setStyleSheet(QFRAME_STYLE)


class Info2(QFrame):
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


class Info3(QFrame):
    def __init__(self, parent, tekst, font):
        super().__init__(parent = parent)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        info=QLabel(tekst)
        info.setStyleSheet(INFO_LABEL_TEXT)        
        info.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        info.setFont(font)

        self.value=QLabel()
        self.value.setStyleSheet(INFO_LABEL_VALUE_2)
        self.value.setAlignment(QtCore.Qt.AlignCenter)
        self.value.setFont(font)

        layout.addWidget(self.value)
        layout.addWidget(info)
        self.setLayout(layout)
        self.setStyleSheet(QFRAME_STYLE)


class Wid(QWidget):
    def __init__(self, parent, tekst, font):
        super().__init__(parent = parent)
        
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        info = QLabel(tekst)
        info.setStyleSheet(INFO_LABEL_TEXT)
        info.setAlignment(QtCore.Qt.AlignCenter)
        info.setFont(font)
        self.value = QLabel()
        self.value.setStyleSheet(INFO_LABEL_VALUE)
        self.value.setAlignment(QtCore.Qt.AlignCenter)
        self.value.setFont(font)

        layout.addWidget(info)
        layout.addWidget(self.value)
        self.setLayout(layout)

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
        self.setStyleSheet(QFRAME_STYLE)