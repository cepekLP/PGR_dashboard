import time
import serial
import os

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


# komunikacja z głównym procesem
class WorkerSignals(QObject):
    error = pyqtSignal(str)
    warning = pyqtSignal(list)
    result = pyqtSignal(list)
    finish = pyqtSignal()


class Worker(QRunnable):
    def __init__(self) -> None:
        super().__init__()
        self.signals = WorkerSignals()
        self.is_killed = False
        self.ser = serial.Serial(
            port="/dev/ttyS0",
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0,
        )

    @pyqtSlot()
    def run(self) -> None:
        i = 0

        while True:
            self.check_serial()

            self.signals.result.emit(["gear", int(i / 10) % 10])
            self.signals.result.emit(["rpm", i * 11 % 19000])
            self.signals.result.emit(["speed", i % 200])
            self.signals.result.emit(["water_temp", i % 200])
            self.signals.result.emit(["oil_temp", i % 200])
            self.signals.result.emit(["break_balance", i % 100])
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

    def check_serial(self) -> None:
        data = self.ser.readline()
        if len(data) and data[:3] == "132" and data[-5:-2] == "792":
            if data[3] == "1":
                os.system("sudo shutdown now")
            if data[4] != 0:
                self.signals.result.emit(["TCS", data[4]])

    # zatrzymanie wątku
    def kill(self) -> None:
        self.is_killed = True
