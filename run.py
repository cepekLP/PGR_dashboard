import logging
import sys
import os
import json
from time import gmtime, strftime
from typing import List, Dict, Tuple, Union
from multiprocessing import Process, Pipe

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

from GUI.MainView import MainView
from GUI.SecondView import SecondView
from GUI.ThirdView import ThirdView

import Workers.httpServer as httpServer

if os.uname()[4] == "armv7l":
    RUNNING_ON_RPI = True
    SHOW_FULLSCREEN = True
    from Workers.CAN_Manager import CAN_Manager
    from Workers.SERIAL_Manager import SERIAL_Manager

    # from Workers.LED_Bar import LED_Bar
else:
    RUNNING_ON_RPI = False
    SHOW_FULLSCREEN = False


NUMBER_OF_VIEWS = 3
DEBUG = True

bolide_info_: Dict[str, Union[int, float]] = {
    "gear": 0,
    "gear_status": 0,
    "rpm": 0,
    "speed": 0,
    "water_temp": 0,
    "oil_temp": 0,
    "oil_press": 0,
    "air_intake_temp": 0.0,
    "voltage": 0.0,
    "TCS": 0,
    "break_balance": 0.0,
}


class MainSignals(QtCore.QObject):
    kill = QtCore.pyqtSignal()
    update = QtCore.pyqtSignal(dict)


class DashBoard(QMainWindow):
    def __init__(
        self, screen_width: int = 1024, screen_height: int = 600
    ) -> None:
        super().__init__()

        self.setStyleSheet("background-color: black")
        self.setFixedSize(screen_width, screen_height)
        self.setCursor(QtCore.Qt.BlankCursor)

        # załadowanie czcionek
        QtGui.QFontDatabase.addApplicationFont(
            "GUI/fonts/digital-7 (mono).ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            "GUI/fonts/LEMONMILK-Regular.otf"
        )

        """id = QtGui.QFontDatabase.addApplicationFont(
            "GUI/fonts/LEMONMILK-Regular.otf",
        )
        #wyświetla nazwe czcionki
        print(QtGui.QFontDatabase.applicationFontFamilies(id))
        """

        self.main_view = MainView(screen_width, screen_height)
        self.second_view = SecondView(screen_width, screen_height)
        self.third_view = ThirdView(screen_width, screen_height)

        # obsługa wielu widoków
        self.layout = QStackedLayout()
        self.layout.addWidget(self.main_view)
        self.layout.addWidget(self.second_view)
        self.layout.addWidget(self.third_view)

        self.layout.setCurrentIndex(self.current_layout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.bolide_info: Dict[str, Union[int, float]] = bolide_info_
        self.current_layout: int = 0

        # obsługa Workers przez osobny proces
        self.threadpool = QtCore.QThreadPool()
        self.signals = MainSignals()
        if RUNNING_ON_RPI is True:
            self.start_threads()

        if DEBUG is True:
            self.pipe, pipe = Pipe()
            self.httpServer = Process(target=httpServer.main, args=(pipe,))
            self.httpServer.start()
            self.pipe.send(json.dumps(self.bolide_info))

        # if RUNNING_ON_RPI:S
        #   self.led_bar = LED_Bar()

        # config logow
        logging.basicConfig(
            format="%(asctime)s | %(levelname)s: %(message)s",
            filename="log/" + strftime("%d-%m-%y_%H%M%S", gmtime()) + ".log",
            level=logging.INFO,
        )
        logging.info("Started...")

        timer = QtCore.QTimer()
        timer.setInterval(250)
        timer.timeout.connect(self.logger)
        timer.start()

    def start_threads(self) -> None:
        CAN = CAN_Manager()
        CAN.signals.result.connect(self.update_info)
        CAN.signals.warning.connect(self.update_warning)
        CAN.signals.error.connect(self.worker_error)
        self.signals.kill.connect(CAN.kill)
        self.threadpool.start(CAN)
        SERIAL = SERIAL_Manager()
        SERIAL.signals.result.connect(self.update_info)
        SERIAL.signals.warning.connect(self.update_warning)
        SERIAL.signals.error.connect(self.worker_error)
        self.signals.kill.connect(SERIAL.kill)
        self.threadpool.start(SERIAL)

    def keyPressEvent(self, event: QtCore.QEvent) -> None:
        if event.key() == QtCore.Qt.Key_Q:
            self.signals.kill.emit()
            self.close()
        elif event.key() == QtCore.Qt.Key_W:
            self.current_layout = (self.current_layout - 1) % NUMBER_OF_VIEWS
        elif event.key() == QtCore.Qt.Key_E:
            self.current_layout = (self.current_layout + 1) % NUMBER_OF_VIEWS
        else:
            pass

        self.layout.setCurrentIndex(self.current_layout)

    def mousePressEvent(self, event: QtCore.QEvent) -> None:
        if event.x() < self.width() / 2:
            self.current_layout = (self.current_layout - 1) % NUMBER_OF_VIEWS
        else:
            self.current_layout = (self.current_layout + 1) % NUMBER_OF_VIEWS

        self.layout.setCurrentIndex(self.current_layout)

    def update_info(self, info: Tuple[str, Union[float, int]]) -> None:
        if info[0] in self.bolide_info:
            self.bolide_info[info[0]] = info[1]

        if self.current_layout == 0:
            self.main_view.update(self.bolide_info)
        elif self.current_layout == 1:
            self.second_view.update(self.bolide_info)
        elif self.current_layout == 2:
            self.third_view.update(self.bolide_info)

        self.signals.update.emit(self.bolide_info)
        if DEBUG is True:
            self.pipe.send(json.dumps(self.bolide_info))
        # if info[0] == "rpm" and RUNNING_ON_RPI:
        #    self.led_bar.update(info[1])

    def update_warning(self, warning: List[str]) -> None:
        if self.current_layout == 0:
            self.main_view.update_warning(warning)
        elif self.current_layout == 1:
            self.second_view.update_warning(warning)
        elif self.current_layout == 2:
            self.third_view.update_warning(warning)

    def worker_error(self, error: str) -> None:
        logging.critical(error)

    def logger(self) -> None:
        # zapis do logu informacji w formie słownika
        logging.info(self.bolide_info)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    if SHOW_FULLSCREEN:
        size = app.desktop().screenGeometry()
        width, height = size.width(), size.height()
        window = DashBoard(width, height)
        window.showFullScreen()
    else:
        window = DashBoard()
        window.show()

    app.exec_()
