import sys
import logging
from time import gmtime, strftime

try:
    import RPi.GPIO as GPIO #zmiana na gpiozero ??
    running_on_RPi = True
    SHOW_FULLSCREEN = True
except:
    running_on_RPi = False
    SHOW_FULLSCREEN = False

from GUI.MainView import MainView
from GUI.SecondView import SecondView
from CAN.CAN_Manager import Worker


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

NUMBER_OF_VIEWS = 2


class BolideInfo:
    gear = 0
    rpm = 0
    break_balance = 0
    speed = 0
    water_temp = 0
    oil_temp = 0
    race_tcs_mode = 0


class ExtendedBolideInfo:
    wheel_temp_1 = 0
    wheel_temp_2 = 0
    wheel_temp_3 = 0
    wheel_temp_4 = 0
    voltage = 0
    oil_pres =0


class DashBoard(QMainWindow):
    def __init__(self, screen_width=800, screen_height=480):
        super().__init__()
        
        self.setStyleSheet("background-color: black")
        self.setFixedSize(screen_width, screen_height)

        #załadowanie czcionek
        QtGui.QFontDatabase.addApplicationFont("GUI/fonts/digital-7 (mono).ttf")
        id = QtGui.QFontDatabase.addApplicationFont("GUI/fonts/LEMONMILK-Regular.otf")
        #print(QtGui.QFontDatabase.applicationFontFamilies(id))
        
        #obsługa CAN przez osobny proces
        self.threadpool = QtCore.QThreadPool()
        self.worker = Worker()
        self.worker.signals.result.connect(self.update)
        self.worker.signals.warning.connect(self.update_warning)
        self.worker.signals.error.connect(self.worker_error)
        self.threadpool.start(self.worker)
        
        self.bolide_info = BolideInfo()
        
        self.main_view = MainView(screen_width, screen_height)
        self.second_view = SecondView(screen_width, screen_height)

        #obłsuga wielu widoków
        self.layout = QStackedLayout()
        self.layout.addWidget(self.main_view)
        self.layout.addWidget(self.second_view)
        
        self.i = 0
        self.layout.setCurrentIndex(self.i)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget) 
        
        #konfig logow
        logging.basicConfig(format="%(asctime)s | %(levelname)s: %(message)s",
                            filename="log/" + strftime("%d-%m-%y %H;%M;%S", gmtime()) + ".log", level=logging.INFO)
        logging.info("Started")

        self.timer = QtCore.QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.logger)
        self.timer.start()


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.worker.kill()
            self.close()
        elif event.key() == QtCore.Qt.Key_W:
            self.i = (self.i - 1) % NUMBER_OF_VIEWS
        elif event.key() == QtCore.Qt.Key_E:
            self.i = (self.i + 1) % NUMBER_OF_VIEWS
        elif event.key() == QtCore.Qt.Key_R:
                self.main_view.warning.delete()
                self.second_view.warning.delete()
        else:
            pass
        self.layout.setCurrentIndex(self.i)
        

    def update(self, str):
        if str[0] == "gear":
            self.bolide_info.gear = str[1]
        elif str[0] == "rpm":
            self.bolide_info.rpm = str[1]
        elif str[0] == "speed":
            self.bolide_info.speed = str[1]
        elif str[0] == "water_temp":
            self.bolide_info.water_temp = str[1]
        elif str[0] == "oil_temp":
            self.bolide_info.oil_temp = str[1]
        elif str[0] == "break_balance":
            self.bolide_info.break_balance = str[1]
        elif str[0] == "TCS":
            self.bolide_info.race_tcs_mode = str[1]
        
        if self.i == 0:
            self.main_view.update(self.bolide_info)
        elif self.i == 1:
            self.second_view.update(self.bolide_info)       


    #dodanie ostrzeżenia
    def update_warning(self, info):
        if info[0]=="ACK":
            self.main_view.warning.delete()
            self.second_view.warning.delete()
        else:
            self.main_view.warning.add(info)
            self.second_view.warning.add(info)
            if info[0] == "error":
                logging.error(info[1])
            elif info[0] == "warning":
                logging.warning(info[1])
            elif info[0] == "info":
                logging.info(info[1])


    def worker_error(self, error):
        logging.critical(error)


    def logger(self):
        logging.info(self.bolide_info.__dict__)     #zapis do logu informacji w formie słownika

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if running_on_RPi:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(21, GPIO.OUT)        #po co?
        GPIO.output(21, GPIO.HIGH)

    if SHOW_FULLSCREEN:
        size = app.desktop().screenGeometry()
        width, height = size.width(), size.height()
        window = DashBoard(width, height)
    else:
        window = DashBoard()
    
    if SHOW_FULLSCREEN:
        window.showFullScreen()
    else:
        window.show()

    app.exec_()
