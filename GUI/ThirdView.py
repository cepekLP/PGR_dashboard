from GUI.styles import *

from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QWidget


class ThirdView(QWidget):
    def __init__(self, width=800, height=480):
        super().__init__()

        self.setFixedSize(width, height)
        self.font = QtGui.QFont('Digital-7 Mono')
        self.font2 = QtGui.QFont('LEMON MILK')
        uic.loadUi("GUI/thirdview.ui", self)
       
        self.gear_value.setStyleSheet(INFO_GEAR)
        self.rpm_unit.setStyleSheet(UNIT_RPM)
        self.rpm_value.setStyleSheet(INFO_RPM)
        self.speed_unit.setStyleSheet(UNIT_RPM)
        self.speed_value.setStyleSheet(INFO_RPM)

        self.water_temp_info.setStyleSheet(INFO_LABEL_TEXT)
        self.water_temp_value.setStyleSheet(INFO_LABEL_VALUE)
        self.oil_temp_info.setStyleSheet(INFO_LABEL_TEXT)
        self.oil_temp_value.setStyleSheet(INFO_LABEL_VALUE)
        self.intake_temp_info.setStyleSheet(INFO_LABEL_TEXT)
        self.intake_temp_value.setStyleSheet(INFO_LABEL_VALUE)
        self.break_balance_info.setStyleSheet(INFO_LABEL_TEXT)
        self.break_balance_value.setStyleSheet(INFO_LABEL_VALUE)
        self.info1_info.setStyleSheet(INFO_LABEL_TEXT)
        self.info1_value.setStyleSheet(INFO_LABEL_VALUE)
        self.info2_info.setStyleSheet(INFO_LABEL_TEXT)
        self.info2_value.setStyleSheet(INFO_LABEL_VALUE)

        self.verticalLayoutWidget.setStyleSheet("background-color: rgba(0, 0, 0, 0%)")
        self.verticalLayoutWidget_2.setStyleSheet("background-color: rgba(0, 0, 0, 0%)")

        self.TCS_info.setStyleSheet(INFO_LABEL_TEXT)
        self.TCS_value.setStyleSheet(INFO_LABEL_VALUE)
        self.test_info.setStyleSheet(INFO_LABEL_TEXT)
        self.test_value.setStyleSheet(INFO_LABEL_VALUE)

        self.warning_value.setStyleSheet("color:white;")

        self.setStyleSheet(QFRAME_STYLE)


    def update(self, display_info):
        self.gear_value.setText(str(display_info['gear']))        
        self.rpm_value.setText(str(display_info['rpm']))  
        self.speed_value.setText(str(display_info['speed']))
        self.water_temp_value.setText(str(display_info['water_temp']))
        self.oil_temp_value.setText(str(display_info['oil_temp']))
        #self.intake_temp_value.setText("
        #{}°C".format(display_info['intake_temp']))
        self.break_balance_value.setText(str(display_info['break_balance']))
        self.TCS_value.setText(str(display_info['TCS']))       
        

    def update_warning(self, info):
        if len(info)==0:
            self.warning_value.setStyleSheet(WARNING_QFRAME_STYLE % (0, 0, 0))
            self.warning_value.setText("")
        else:
            if info[0][0] == 0:
                self.warning_value.setStyleSheet(WARNING_QFRAME_STYLE % (255, 0, 0))
            elif info[0][0] == 1:
                self.warning_value.setStyleSheet(WARNING_QFRAME_STYLE % (255, 128, 0))
            elif info[0][0] == 2:
                self.warning_value.setStyleSheet(WARNING_QFRAME_STYLE % (0, 192, 0))
            
            self.warning_value.setText(info[0][1])

