import time

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict)

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        i = 0
        while True:
            self.signals.result.emit({"name" : "gear",  "value" : i % 10})     
            self.signals.result.emit({"name" : "rpm",   "value" : i % 19000})
            self.signals.result.emit({"name" : "speed", "value" : i % 200})
            i=i+1
            time.sleep(0.1)