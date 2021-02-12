import sys
import logging
from time import gmtime, strftime

try:
    import gpiozero as GPIO
    running_on_RPi = True
    SHOW_FULLSCREEN = True
except:
    running_on_RPi = False
    SHOW_FULLSCREEN = False

from GUI.MainView import MainView
from GUI.SecondView import SecondView
from GUI.ThirdView import ThirdView
from CAN.CAN_Manager import Worker
from server.server import Server


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

NUMBER_OF_VIEWS = 3


bolide_info_ = {
    'gear' : 0,
    'rpm' : 0,
    'break_balance' : 0,
    'speed' : 0,
    'water_temp' : 0,
    'oil_temp' : 0,
    'air_intake_temp' : 0,
    'race_tcs_mode' : 0
    }

extended_bolide_info_ = {
    'wheel_temp_1' : 0,
    'wheel_temp_2' : 0,
    'wheel_temp_3' : 0,
    'wheel_temp_4' : 0,
    'voltage' : 0,
    'oil_press' : 0
    }

class MainSignals(QtCore.QObject):
    kill = QtCore.pyqtSignal()
    update = QtCore.pyqtSignal(dict)


class DashBoard(QMainWindow):
    bolide_info = bolide_info_
    current_layout = 0
    def __init__(self, screen_width=800, screen_height=480):
        super().__init__()
        
        self.setStyleSheet("background-color: black")
        self.setFixedSize(screen_width, screen_height)
        self.setCursor(QtCore.Qt.BlankCursor)    

        #załadowanie czcionek
        QtGui.QFontDatabase.addApplicationFont("GUI/fonts/digital-7 (mono).ttf")
        id = QtGui.QFontDatabase.addApplicationFont("GUI/fonts/LEMONMILK-Regular.otf")
        #wyświetla nazwe czcionki
        #print(QtGui.QFontDatabase.applicationFontFamilies(id))
        
        #obsługa CAN przez osobny proces
        self.threadpool = QtCore.QThreadPool()
        self.signals = MainSignals()
        self.start_threads()
        
        self.main_view = MainView(screen_width, screen_height)
        self.second_view = SecondView(screen_width, screen_height)
        self.third_view = ThirdView(screen_width, screen_height)

        #obsługa wielu widoków
        self.layout = QStackedLayout()
        self.layout.addWidget(self.main_view)
        self.layout.addWidget(self.second_view)
        self.layout.addWidget(self.third_view)
        
        self.layout.setCurrentIndex(self.current_layout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget) 
       
        #config logow
        logging.basicConfig(format="%(asctime)s | %(levelname)s: %(message)s",
                            filename="log/" + strftime("%d-%m-%y_%H%M%S", gmtime()) + ".log", level=logging.INFO)
        logging.info("Started...")

        self.timer = QtCore.QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.logger)
        self.timer.start()


    def start_threads(self):
        worker = Worker()
        worker.signals.result.connect(self.update)
        worker.signals.warning.connect(self.update_warning)
        worker.signals.error.connect(self.worker_error)
        self.signals.kill.connect(worker.kill)
        self.threadpool.start(worker)
        
        server = Server()
        server.signals.warning.connect(self.update_warning)
        self.signals.kill.connect(server.kill)
        self.signals.update.connect(server.update)
        self.threadpool.start(server)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.singals.kill.emit()
            self.close()
        elif event.key() == QtCore.Qt.Key_W:
            self.i = (self.current_layout - 1) % NUMBER_OF_VIEWS
        elif event.key() == QtCore.Qt.Key_E:
            self.i = (self.current_layout + 1) % NUMBER_OF_VIEWS
        elif event.key() == QtCore.Qt.Key_R:
                self.main_view.warning.delete()
                self.second_view.warning.delete()
        else:
            pass
        self.layout.setCurrentIndex(self.current_layout)
        

    def mousePressEvent(self, event):
        if event.x() > self.width() / 2 and event.y() > self.height() / 3 * 2:
            self.main_view.warning.delete()
            self.second_view.warning.delete()
        elif event.x() < self.width() / 2:
            self.current_layout = (self.current_layout - 1) % NUMBER_OF_VIEWS
        else:
            self.current_layout = (self.current_layout + 1) % NUMBER_OF_VIEWS
        
        self.layout.setCurrentIndex(self.current_layout)


    def update(self, str):
        if str[0] in self.bolide_info:
            self.bolide_info[str[0]] = str[1]
        
        if self.current_layout == 0:
            self.main_view.update(self.bolide_info)
        elif self.current_layout == 1:
            self.second_view.update(self.bolide_info)    

        self.signals.update.emit(self.bolide_info)


    def update_warning(self, info):
        if info[0] == "ACK":
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
        logging.info(self.bolide_info)     #zapis do logu informacji w formie słownika
if __name__ == '__main__':
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
