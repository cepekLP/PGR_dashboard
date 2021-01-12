try:
    from DashBoard.GUI.styles import *
except:
    from GUI.styles import *

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLCDNumber, QLabel, QProgressBar, QWidget, QHBoxLayout, QFrame


class MainView(QWidget):
    def __init__(self, main_window):
        super(MainView, self).__init__()

        self.setFixedSize(main_window.width(), main_window.height())
        self.font = QtGui.QFont('Seven Segment')

        self.gear_LCD = QLabel(main_window)
        self.init_gear_LCD()

        #self.rpm_progressbar = QProgressBar(main_window)
        #self.init_rpm_progressbar()

       # self.break_progressbar = QProgressBar(main_window)
        #self.init_break_progressbar()

        #self.rpm_LCD = QLabel(main_window)
        #self.label_rpm = QLabel(main_window)
       
        self.rpm = Wid2(main_window)    
        self.init_rpm()

        self.speed = Wid2(main_window)        
        self.init_speed()

       #self.water_temp_label = QLabel(main_window)
        #self.init_water_temp()

        #self.oil_temp_label = QLabel(main_window)
        #self.init_oil_temp()

        #self.RTCS_mode_label = QLabel(main_window)
        #self.init_RTCS_mode()

    def init_gear_LCD(self):
        self.gear_LCD.setFixedSize(GEAR_SIZE * 0.65, GEAR_SIZE)
        self.gear_LCD.move((int(self.width()) - GEAR_SIZE * 0.65) / 2 , 0)
        self.gear_LCD.setFont(self.font)
        self.gear_LCD.setAlignment(QtCore.Qt.AlignCenter)
        self.gear_LCD.setStyleSheet(INFO_GEAR)
        self.gear_LCD.setText('n')

    def init_rpm_progressbar(self):
        self.rpm_progressbar.setOrientation(QtCore.Qt.Vertical)
        self.rpm_progressbar.setFixedSize(int(self.width() * 0.05), int(self.height() - 2 * OFFSET))
        self.rpm_progressbar.move(OFFSET, OFFSET)
        self.rpm_progressbar.setStyleSheet(PROGRESS_BAR_STYLES % ("white", "white"))
        self.rpm_progressbar.setValue(80)
        self.rpm_progressbar.setTextVisible(False)

    def init_break_progressbar(self):
        self.break_progressbar.setOrientation(QtCore.Qt.Vertical)
        self.break_progressbar.setFixedSize(int(self.width() * 0.05), int(0.5 * self.height()))
        self.break_progressbar.move(self.width() - self.break_progressbar.width() - OFFSET, 0.25 * self.height())
        self.break_progressbar.setStyleSheet(PROGRESS_BAR_STYLES % ("yellow", "yellow"))
        self.break_progressbar.setValue(80)
        self.break_progressbar.setTextVisible(False)

    def init_rpm(self):
        self.rpm.setFixedSize(GEAR_SIZE * 2 + OFFSET, GEAR_SIZE * 0.75)
        self.rpm.move(int((self.width() - GEAR_SIZE * 0.65) / 2) - self.rpm.width() + 5, GEAR_SIZE / 8)
        
        
        self.rpm.value.setFixedSize(GEAR_SIZE * 1.5, GEAR_SIZE / 2)       
        self.rpm.value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.rpm.value.setText('12000')
        self.rpm.value.setStyleSheet(INFO_RPM)
        
        self.rpm.unit.setFont(self.font)
        self.rpm.unit.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.rpm.unit.setStyleSheet(INFO_LABEL_STYLES)
        self.rpm.unit.setText('RPM')

    def init_speed(self):
        self.speed.setFixedSize(GEAR_SIZE * 2 + OFFSET, GEAR_SIZE * 0.75)
        self.speed.move(int((self.width() + GEAR_SIZE * 0.65) / 2) - 5, GEAR_SIZE / 8)
        
        self.speed.value.setFixedSize(GEAR_SIZE * 1.5, GEAR_SIZE / 2)       
        self.speed.value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.speed.value.setText('120')
        self.speed.value.setStyleSheet(INFO_RPM)
        
        self.speed.unit.setFont(self.font)
        self.speed.unit.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.speed.unit.setStyleSheet(INFO_LABEL_STYLES)
        self.speed.unit.setText('KMPH')

    def init_water_temp(self):
        self.water_temp_label.setFixedSize(self.width() * 0.25, self.height() * 0.3)
        self.water_temp_label.move(self.rpm_progressbar.width() + 2 * OFFSET,
                                   self.height() - self.water_temp_label.height() - OFFSET)
        self.water_temp_label.setStyleSheet(STATUS_LABEL_STYLES % (self.height() / 10, 'blue'))
        self.water_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.water_temp_label.setText("WATER:\n100°C")

    def init_oil_temp(self):
        self.oil_temp_label.setFixedSize(self.width() * 0.25, self.height() * 0.3)
        self.oil_temp_label.move(self.rpm_progressbar.width() + self.water_temp_label.width() + 3 * OFFSET,
                                 self.height() - self.oil_temp_label.height() - OFFSET)
        self.oil_temp_label.setStyleSheet(STATUS_LABEL_STYLES % (self.height() / 10, 'darkorange'))
        self.oil_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.oil_temp_label.setText("OIL:\n100°C")

    def init_RTCS_mode(self):
        self.RTCS_mode_label.setFixedSize(self.width() * 0.25, self.height() * 0.3)
        self.RTCS_mode_label.move(self.rpm_progressbar.width() + 2 * self.water_temp_label.width() + 4 * OFFSET,
                                  self.height() - self.oil_temp_label.height() - OFFSET)
        self.RTCS_mode_label.setStyleSheet(STATUS_LABEL_STYLES % (self.height() / 10, 'yellow'))
        self.RTCS_mode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RTCS_mode_label.setText("RTCS:\n1")

    def update_main_view(self, display_info):
        self.gear_LCD.display(display_info.gear)
        self.rpm_progressbar.setValue(display_info.rpm)
        self.rpm_LCD.display(display_info.rpm)
        self.break_progressbar.setValue(display_info.break_balance)
        self.speed_LCD.display(display_info.speed)
        self.water_temp_label.setText("WATER:\n{}°C".format(display_info.water_temp))
        self.oil_temp_label.setText("OIL:\n{}°C".format(display_info.oil_temp))
        self.RTCS_mode_label.setText("RTCS:\n{}".format(display_info.race_tcs_mode))

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

class Wid(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.value = QLabel('123')
        self.unit = QLabel()
        
        layout.addWidget(self.value)       
        layout.addWidget(self.unit)

        self.setLayout(layout)

class Wid2(QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent) 
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        self.value = QLabel()
        self.unit = QLabel()

        self.value.setFont(QtGui.QFont('Seven Segment'))
        self.unit.setFont(QtGui.QFont('Seven Segment'))
        
        layout.addWidget(self.value)       
        layout.addWidget(self.unit)

        self.setLayout(layout)
        self.setStyleSheet(DISPLAY_STYLE)