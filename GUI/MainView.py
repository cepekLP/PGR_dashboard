try:
    from GUI.styles import *
except:
    from Dashboard.GUI.styles import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber, QLabel, QProgressBar, QWidget, QFrame


class MainView(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.setFixedSize(main_window.width(), main_window.height())
        self.font = QtGui.QFont('Digital-7 Mono')
        self.font2 = QtGui.QFont('LEMON MILK')

        self.gear_LCD = QLabel(main_window)
        self.init_gear_LCD()
       
        self.rpm = Wid2(main_window, self.font)    
        self.init_rpm()

        self.speed = Wid2(main_window, self.font)        
        self.init_speed()

        self.info = Info(main_window, self.font2)
        self.init_info()

        self.warning = Warning(main_window, self.font2)
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
        self.rpm.value.move(GEAR_SIZE, 200)
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
        self.info.setFixedSize(int(self.width()/2), self.height()-GEAR_SIZE)
        self.info.move(0, GEAR_SIZE)
        self.info.water_temp.setText('  100°C')
        self.info.oil_temp.setText('  100°C')
        self.info.break_balance.setText('0')
        self.info.TCS.setText('0')

    
    def init_warning(self):
        self.warning.setFixedSize(int(self.width() /2), int((self.height()-GEAR_SIZE)/2))
        self.warning.move(int(self.width() /2), GEAR_SIZE)


    def update(self, display_info):
        self.gear_LCD.setText(str(display_info.gear))        
        self.rpm.value.setText(str(display_info.rpm))  
        self.speed.value.setText(str(display_info.speed))
        self.info.water_temp.setText("{}°C".format(display_info.water_temp))
        self.info.oil_temp.setText("{}°C".format(display_info.oil_temp))
        self.info.break_balance.setText(str(display_info.break_balance))
        self.info.TCS.setText(str(display_info.race_tcs_mode))     


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


    def setVisible(self, visibility):
        self.gear_LCD.setVisible(visibility)
        self.rpm_progressbar.setVisible(visibility)
        self.break_progressbar.setVisible(visibility)
        self.rpm_LCD.setVisible(visibility)
        self.speed_LCD.setVisible(visibility)
        self.label_rpm.setVisible(visibility)
        self.label_speed.setVisible(visibility)
        self.water_temp_label.setVisible(visibility)
        self.oil_temp_label.setVisible(visibility)
        self.RTCS_mode_label.setVisible(visibility)


class Wid2(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent) 
        self.setFixedSize(int((parent.width() - GEAR_SIZE * 0.65) / 2), GEAR_SIZE)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
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

        layout2 = QtWidgets.QHBoxLayout()
        water_temp_text = QLabel("Water temp")
        water_temp_text.setStyleSheet(INFO_LABEL_TEXT)
        water_temp_text.setAlignment(QtCore.Qt.AlignCenter)
        water_temp_text.setFont(font)
        self.water_temp = QLabel()
        self.water_temp.setStyleSheet(INFO_LABEL_VALUE)
        self.water_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.water_temp.setFont(font)
        layout2.addWidget(water_temp_text)
        layout2.addWidget(self.water_temp)

        layout3 = QtWidgets.QHBoxLayout()
        oil_temp_text = QLabel("Oil temp")
        oil_temp_text.setStyleSheet(INFO_LABEL_TEXT)
        oil_temp_text.setAlignment(QtCore.Qt.AlignCenter)
        oil_temp_text.setFont(font)
        self.oil_temp = QLabel()
        self.oil_temp.setStyleSheet(INFO_LABEL_VALUE)
        self.oil_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.oil_temp.setFont(font)
        layout3.addWidget(oil_temp_text)
        layout3.addWidget(self.oil_temp)

        layout4 = QtWidgets.QHBoxLayout()
        break_balance_text = QLabel("Break balance")
        break_balance_text.setStyleSheet(INFO_LABEL_TEXT)
        break_balance_text.setAlignment(QtCore.Qt.AlignCenter)
        break_balance_text.setFont(font)
        self.break_balance = QLabel()
        self.break_balance.setStyleSheet(INFO_LABEL_VALUE)
        self.break_balance.setAlignment(QtCore.Qt.AlignCenter)
        self.break_balance.setFont(font)
        layout4.addWidget(break_balance_text)
        layout4.addWidget(self.break_balance)

        layout5 = QtWidgets.QHBoxLayout()
        TCS_text = QLabel("TCS")
        TCS_text.setStyleSheet(INFO_LABEL_TEXT)
        TCS_text.setAlignment(QtCore.Qt.AlignCenter)
        TCS_text.setFont(font)
        self.TCS = QLabel()
        self.TCS.setStyleSheet(INFO_LABEL_VALUE)
        self.TCS.setAlignment(QtCore.Qt.AlignCenter)
        self.TCS.setFont(font)
        layout5.addWidget(TCS_text)
        layout5.addWidget(self.TCS)

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        layout1.addLayout(layout4)
        layout1.addLayout(layout5)        
        
          
        layout1.addChildLayout(layout5)
        
        self.setLayout(layout1)
        self.setStyleSheet(QFRAME_STYLE)


class Warning(QFrame):
    def __init__(self, parent, font):
        super().__init__(parent = parent)
        layout = QtWidgets.QVBoxLayout()
        
        self.tekst = QLabel()
        self.tekst.setStyleSheet(INFO_LABEL_VALUE + "color: black; font-size: 30px;")
        self.tekst.setAlignment(QtCore.Qt.AlignCenter)
        self.tekst.setWordWrap(True)
        self.tekst.setFont(font)
        layout.addWidget(self.tekst)
        
        self.setLayout(layout)
        self.setStyleSheet(QFRAME_STYLE)