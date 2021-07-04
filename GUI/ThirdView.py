import GUI.styles as st
from typing import Dict, List

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QWidget


class ThirdView(QWidget):
    def __init__(self, width: int = 800, height: int = 480) -> None:
        super().__init__()

        self.setFixedSize(width, height)
        self.font = QtGui.QFont("Digital-7 Mono")
        self.font2 = QtGui.QFont("LEMON MILK")
        uic.loadUi("GUI/thirdview.ui", self)

        self.gear_value.setStyleSheet(st.INFO_GEAR)

        self.rpm_bar_G.setStyleSheet(st.RPM_BAR % (0, 255, 0))
        self.rpm_bar_Y.setStyleSheet(st.RPM_BAR % (255, 255, 0))
        self.rpm_bar_R.setStyleSheet(st.RPM_BAR % (255, 0, 0))
        self.rpm_unit.setStyleSheet(st.UNIT_RPM)
        self.rpm_value.setStyleSheet(st.INFO_RPM)

        self.water_temp_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.water_temp_value.setStyleSheet(st.INFO_LABEL_VALUE)
        self.oil_temp_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.oil_temp_value.setStyleSheet(st.INFO_LABEL_VALUE)
        self.intake_temp_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.intake_temp_value.setStyleSheet(st.INFO_LABEL_VALUE)
        self.break_balance_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.break_balance_value.setStyleSheet(st.INFO_LABEL_VALUE)
        self.info1_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.info1_value.setStyleSheet(st.INFO_LABEL_VALUE)

        self.verticalLayoutWidget.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0%)"
        )
        self.verticalLayoutWidget_2.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0%)"
        )

        self.TCS_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.TCS_value.setStyleSheet(st.INFO_LABEL_VALUE)
        self.test_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.test_value.setStyleSheet(st.INFO_LABEL_VALUE)

        self.warning_value.setStyleSheet("color:white;")

        self.setStyleSheet(st.QFRAME_STYLE)

    def update(self, display_info: Dict[str, int]) -> None:
        self.gear_value.setText(str(display_info["gear"]))

        self.rpm_value.setText(str(display_info["rpm"]))
        self.update_bar(display_info["rpm"])

        self.water_temp_value.setText(str(display_info["water_temp"]))
        self.oil_temp_value.setText(str(display_info["oil_temp"]))
        # self.intake_temp_value.setText("
        # {}°C".format(display_info['intake_temp']))
        self.break_balance_value.setText(str(display_info["break_balance"]))
        self.TCS_value.setText(str(display_info["TCS"]))

    def update_bar(self, rpm: int) -> None:
        if rpm <= 7000:
            self.rpm_bar_G.setValue(rpm)
            self.rpm_bar_Y.setValue(0)
            self.rpm_bar_R.setValue(0)

        elif rpm <= 10250:
            self.rpm_bar_G.setValue(7000)
            self.rpm_bar_Y.setValue(rpm - 7000)
            self.rpm_bar_R.setValue(0)
        else:
            self.rpm_bar_G.setValue(7000)
            self.rpm_bar_Y.setValue(3250)
            self.rpm_bar_R.setValue(rpm - 10250)

    def update_warning(self, warning: List[str]) -> None:
        if warning[0] == "error":
            self.warning_value.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (255, 0, 0)
            )
        elif warning[0] == "warning":
            self.warning_value.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (255, 128, 0)
            )
        elif warning[0] == "info":
            self.warning_value.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (0, 192, 0)
            )

        self.warning_value.setText(warning[1])
