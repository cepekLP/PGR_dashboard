import serial
import os

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


class WorkerSignals(QObject):
    error = pyqtSignal(str)
    warning = pyqtSignal(list)
    result = pyqtSignal(list)
    finish = pyqtSignal()


class SERIAL_Manager(QRunnable):
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
            timeout=1,
        )

    @pyqtSlot()
    def run(self) -> None:
        while True:
            data = self.ser.readline().decode("utf-8")
            if len(data) > 6:
                if len(data) and data[:3] == "132" and data[-5:-2] == "792":
                    if data[3] == "1":
                        self.signals.warning.emit(["info", "SHUT DOWN"])
                        os.system("sudo shutdown now")
                    if data[4] != 0:
                        self.signals.result.emit(["TCS", data[4]])

    # zatrzymanie wątku
    def kill(self) -> None:
        self.is_killed = True
