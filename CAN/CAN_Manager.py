import time

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

#komunikacja z głównym procesem
class WorkerSignals(QObject):
    error = pyqtSignal(str)
    warning = pyqtSignal(list)
    result = pyqtSignal(list)
    finish = pyqtSignal()


class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
        self.is_killed = False


    @pyqtSlot()
    def run(self):
        i = 0
        #test Wyświetlacza
        while True:
            self.signals.result.emit(["gear",           int(i / 10) % 10])     
            self.signals.result.emit(["rpm",            i * 11 % 19000])
            self.signals.result.emit(["speed",          i % 200])
            self.signals.result.emit(["water_temp",     i % 200])
            self.signals.result.emit(["oil_temp",       i % 200])
            self.signals.result.emit(["break_balance",  i % 100])
            self.signals.result.emit(["TCS",            i % 20])
            i = i + 1
            time.sleep(0.05)
            if i % 150 == 0:
                self.signals.warning.emit(["error", "ERROR TEXT"]) 
            elif (i + 50) % 150 == 0:
                self.signals.warning.emit(["warning", "WARNING TEXT"])
            elif (i + 100) % 150 == 0:
                self.signals.warning.emit(["info", "INFO TEXT"])

            if self.is_killed:
                return
        

    #zatrzymanie wątku
    def kill(self):
        self.is_killed = True


        
