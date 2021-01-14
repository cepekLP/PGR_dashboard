import sys

try:
    import RPi.GPIO as GPIO
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

        QtGui.QFontDatabase.addApplicationFont("GUI/fonts/digital-7 (mono).ttf")
        id = QtGui.QFontDatabase.addApplicationFont("GUI/fonts/LEMONMILK-Regular.otf")
        #print(QtGui.QFontDatabase.applicationFontFamilies(id))

        self.threadpool = QtCore.QThreadPool()
        self.worker = Worker()
        self.worker.signals.result.connect(self.update)
        self.worker.signals.error.connect(self.worker_error)
        self.threadpool.start(self.worker)
        
        self.bolide_info = BolideInfo()
        
        self.main_view=MainView(screen_width, screen_height)
        self.second_view=SecondView()

        self.layout = QStackedLayout()
        self.layout.addWidget(self.main_view)
        self.layout.addWidget(self.second_view)
        
        self.layout.setCurrentIndex(0)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget) 
        
        #self.main_view.update_warning("error" ,"ERROR TEXT")


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.worker.kill()
            self.close()
        elif event.key() == QtCore.Qt.Key_W:
            self.layout.setCurrentIndex(0)  
        elif event.key() == QtCore.Qt.Key_E:
            self.layout.setCurrentIndex(1)  
        else:
            pass
        

    def update(self, str):
        if str["name"] == "gear":
            self.bolide_info.gear = str["value"]
        elif str["name"] == "rpm":
            self.bolide_info.rpm = str["value"]
        elif str["name"] == "speed":
            self.bolide_info.speed = str["value"]
        elif str["name"] == "water_temp":
            self.bolide_info.water_temp = str["value"]
        elif str["name"] == "oil_temp":
            self.bolide_info.oil_temp = str["value"]
        elif str["name"] == "break_balance":
            self.bolide_info.break_balance = str["value"]
        elif str["name"] == "TCS":
            self.bolide_info.race_tcs_mode = str["value"]

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
    
    
    
    if SHOW_FULLSCREEN:
        window.showFullScreen()
    else:
        window.show()

    app.exec_()
