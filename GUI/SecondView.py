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

        self.warning = Warning(self, self.font2)
        self.init_warning()

        self.info_left = Info_Left(self, self.font2)
        self.init_info_left()

        self.info_right = Info_Right(self, self.font2)
        self.init_info_right()        
        
        self.info_vertical = Info_3(self, self.font2)
        self.init_info_vertical()
        

    def init_gear_LCD(self):
        self.gear_LCD.setFixedSize(GEAR_WIDTH, GEAR_HEIGHT)
        self.gear_LCD.move((int(self.width()) - GEAR_WIDTH) / 2 , RPM_HEIGHT)
        self.gear_LCD.setFont(self.font)
        self.gear_LCD.setAlignment(QtCore.Qt.AlignCenter)
        self.gear_LCD.setStyleSheet(INFO_GEAR)
        self.gear_LCD.setText('0')


    def init_rpm(self):
        self.rpm.setFixedSize(int(self.width() / 2), RPM_HEIGHT)
        self.rpm.move(0, 0)       
       
        self.rpm.value.setFixedSize(int(self.width() / 2 - OFFSET), RPM_HEIGHT * 0.75)       
        self.rpm.value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.rpm.value.setText('22000')
        self.rpm.value.setStyleSheet(INFO_RPM_2)
        
        self.rpm.unit.setFixedWidth(int(self.width() / 2 - OFFSET * 1.5))
        self.rpm.unit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.rpm.unit.setStyleSheet(UNIT_RPM)
        self.rpm.unit.setText('RPM')


    def init_speed(self):
        self.speed.setFixedSize(int(self.width() / 2), RPM_HEIGHT)
        self.speed.move(int(self.width() / 2), 0)
        
        self.speed.value.setFixedSize(int((self.width() - GEAR_WIDTH) * 0.33), RPM_HEIGHT * 0.75)
        self.speed.value.setText('220')
        self.speed.value.setStyleSheet(INFO_RPM_2)
        
        self.speed.unit.setFixedWidth(int((self.width() - GEAR_WIDTH) * 0.33))
        self.speed.unit.setStyleSheet(UNIT_RPM)
        self.speed.unit.setText('KMPH')


    def init_info_left(self):
        self.info_left.setFixedSize(int((self.width() - GEAR_WIDTH) / 2), int((self.height() - RPM_HEIGHT) / 2))
        self.info_left.move(0, RPM_HEIGHT)
 
        self.info_left.water_temp.value.setText('0')
        self.info_left.oil_temp.value.setText('0')
        self.info_left.air_intake_temp.value.setText('0')

        
    def init_info_right(self):
        self.info_right.setFixedSize(int((self.width() - GEAR_WIDTH) / 2), int((self.height() - RPM_HEIGHT) / 2))
        self.info_right.move(int((self.width() + GEAR_WIDTH) / 2), RPM_HEIGHT)

        self.info_right.break_balance.value.setText('0')
        self.info_right.info2.value.setText('0')
        self.info_right.info3.value.setText('0')


    def init_info_vertical(self):
        self.info_vertical.setFixedSize(int((self.width() - GEAR_WIDTH) / 2), int((self.height() - RPM_HEIGHT) / 2))
        self.info_vertical.move(0, RPM_HEIGHT * 2)

        self.info_vertical.TCS.value.setText('0')
        self.info_vertical.info4.value.setText('0')
        

    def init_warning(self):
        self.warning.setFixedSize(int((self.width()-GEAR_WIDTH) / 2), int((self.height() - RPM_HEIGHT) / 2))
        self.warning.move(int((self.width()+GEAR_WIDTH) / 2), RPM_HEIGHT + int((self.height() - RPM_HEIGHT) / 2))
        
        self.warning_list = []


    def update(self, display_info):
        self.gear_LCD.setText(str(display_info.gear))        
        self.rpm.value.setText(str(display_info.rpm))  
        self.speed.value.setText(str(display_info.speed))
        self.info_left.water_temp.value.setText("   {}°C".format(display_info.water_temp))
        self.info_left.oil_temp.value.setText("   {}°C".format(display_info.oil_temp))
        self.info_right.break_balance.value.setText(str(display_info.break_balance))
        self.info_vertical.TCS.value.setText(str(display_info.race_tcs_mode))        


class Info_Left(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent)
        layout1 = QtWidgets.QVBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)

        self.water_temp = Wid(parent, "Water", font)
        self.oil_temp = Wid(parent, "Oil", font)
        self.air_intake_temp = Wid(parent, "Air intake", font)
        
        layout1.addWidget(self.water_temp)
        layout1.addWidget(self.oil_temp)
        layout1.addWidget(self.air_intake_temp)
        
        self.setLayout(layout1)
        self.setStyleSheet(QFRAME_STYLE)


class Info_Right(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent)
        layout1 = QtWidgets.QVBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)

        self.break_balance = Wid(parent, "Balance", font)
        self.info2 = Wid(parent, "Info2", font)
        self.info3 = Wid(parent, "Info3", font)
        
        layout1.addWidget(self.break_balance)
        layout1.addWidget(self.info2)
        layout1.addWidget(self.info3)
        
        self.setLayout(layout1)
        self.setStyleSheet(QFRAME_STYLE)


class Info_3(QWidget):
    def __init__(self, parent, font):
        super().__init__(parent=parent)
        
        layout = QtWidgets.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.TCS = Wid2(self, "TCS", font)
        self.info4 = Wid2(self, "Info2", font)

        layout.addWidget(self.TCS)
        layout.addWidget(self.info4)

        self.setLayout(layout)