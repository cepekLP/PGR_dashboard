import GUI.styles as st
from typing import Dict, List, Union, Any

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QWidget

READY = 0
OK = 1
NOT_CHANGED = 2
GEAR_UNKNOWN = 3
DISABLED = 4


class MainView(QWidget):
    def __init__(self, width: int = 800, height: int = 480) -> None:
        super().__init__()

        self.setFixedSize(width, height)
        self.font = QtGui.QFont("Digital-7 Mono")
        self.font2 = QtGui.QFont("LEMON MILK")
        uic.loadUi("GUI/mainview.ui", self)

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
        self.voltage_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.voltage_value.setStyleSheet(st.INFO_LABEL_VALUE)

        self.verticalLayoutWidget.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0%)"
        )
        self.TCS_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.TCS_value.setStyleSheet(st.INFO_LABEL_VALUE)
        self.test_info.setStyleSheet(st.INFO_LABEL_TEXT)
        self.test_value.setStyleSheet(st.INFO_LABEL_VALUE)

        self.warning_value.setStyleSheet("color:white;")

        self.setStyleSheet(st.QFRAME_STYLE)

    def _update_gear_status(self, gear_status: Any) -> None:
        if gear_status == READY:
            self.gear_status.setStyleSheet(st.WARNING_QFRAME_STYLE % (0, 0, 0))
            self.gear_status.setText("READY")
        elif gear_status == OK:
            self.gear_status.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (0, 192, 0)
            )
            self.gear_status.setText("OK")
        elif gear_status == NOT_CHANGED:
            self.gear_status.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (255, 0, 0)
            )
            self.gear_status.setText("NOT CHANGED")
        elif gear_status == GEAR_UNKNOWN:
            self.gear_status.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (74, 74, 74)
            )
            self.gear_status.setText("GEAR_UNKNOWN")
        elif gear_status == DISABLED:
            self.gear_status.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (74, 74, 74)
            )
            self.gear_status.setText("DISABLED")

    def _update_bar(self, rpm: Any) -> None:
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

    def update(self, display_info: Dict[str, Union[int, float]]) -> None:
        self.gear_value.setText(str(display_info["gear"]))
        self._update_gear_status(display_info["gear_status"])
        self.rpm_value.setText(str(int(display_info["rpm"])))
        self._update_bar(display_info["rpm"])

        # self.speed_value.setText(str(display_info["speed"]))
        self.water_temp_value.setText(str(display_info["water_temp"]))
        self.oil_temp_value.setText(str(display_info["oil_temp"]))
        # self.intake_temp_value.setText("
        # {}°C".format(display_info['intake_temp']))
        self.intake_temp_value.setText(str(display_info["air_intake_temp"]))
        self.voltage_value.setText(str(display_info["voltage"]))
        self.TCS_value.setText(str(display_info["TCS"]))

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
        elif warning[0] == "default":
            self.warning_value.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (0, 0, 0)
            )
        elif warning[0] == "disabled":
            self.warning_value.setStyleSheet(
                st.WARNING_QFRAME_STYLE % (74, 74, 74)
            )

        self.warning_value.setText(warning[1])
