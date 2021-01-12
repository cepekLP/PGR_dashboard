import sys

try:
    import RPi.GPIO as GPIO
    running_on_RPi = True
    SHOW_FULLSCREEN = True
except:
    running_on_RPi = False
    SHOW_FULLSCREEN = False

from GUI.MainView import MainView
from CAN.CAN_Manager import Worker


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow




class BolideInfo:
    gear = 0
    rpm = 0
    break_balance = 0
    speed = 0
    water_temp = 0
    oil_temp = 0
    race_tcs_mode = 0


class DashBoard(QMainWindow):
    def __init__(self, screen_width=800, screen_height=480):
        super().__init__()

        self.setStyleSheet("background-color: black")
        self.setFixedSize(screen_width, screen_height)

        self.threadpool = QtCore.QThreadPool()
        worker = Worker()
        worker.signals.result.connect(self.update)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)

        self.bolide_info = BolideInfo()
        self.main_view = MainView(self)      

        if SHOW_FULLSCREEN:
            self.showFullScreen()
        else:
            self.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.close()
        elif event.key() == QtCore.Qt.Key_W:
            self.main_view.setVisible(True)
        elif event.key() == QtCore.Qt.Key_E:
            self.main_view.setVisible(False)
        else:
            pass

    def update(self, str):
        if str["name"] == "gear":
            self.bolide_info.gear = str["value"]
        elif str["name"] == "rpm":
            self.bolide_info.rpm = str["value"]
        elif str["name"] == "speed":
            self.bolide_info.speed = str["value"]

        self.main_view.update(self.bolide_info)

    def worker_error(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    if running_on_RPi:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21, GPIO.HIGH)

    if SHOW_FULLSCREEN:
        size = app.desktop().screenGeometry()
        width, height = size.width(), size.height()
        window = DashBoard(width, height)
    else:
        window = DashBoard()
    
    QtGui.QFontDatabase.addApplicationFont("GUI/SevenSegment.ttf")
    app.exec_()
