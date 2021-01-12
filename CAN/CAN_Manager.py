import time

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

class WorkerSignals(QObject):
    error = pyqtSignal(str)
    result = pyqtSignal(dict)

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
        self.is_killed = False

    @pyqtSlot()
    def run(self):
        i = 0
        try:
            while True:
                self.signals.result.emit({"name" : "gear",          "value" : i % 10})     
                self.signals.result.emit({"name" : "rpm",           "value" : i * 11 % 19000})
                self.signals.result.emit({"name" : "speed",         "value" : i % 200})
                self.signals.result.emit({"name" : "water_temp",    "value" : i % 200})
                self.signals.result.emit({"name" : "oil_temp",      "value" : i % 200})
                self.signals.result.emit({"name" : "break_balance", "value" : i % 100})
                self.signals.result.emit({"name" : "TCS",           "value" : i % 20})
                i = i + 1
                time.sleep(0.1)

            if self.is_killed:
                raise WorkerKilledException

        except WorkerKilledException:
            pass
        
    def kill(self):
        self.is_killed = True


        
