import time
import os
import can

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


# komunikacja z głównym procesem
class WorkerSignals(QObject):
    error = pyqtSignal(str)
    warning = pyqtSignal(list)
    result = pyqtSignal(list)
    finish = pyqtSignal()


class CAN_Manager(QRunnable):
    def __init__(self) -> None:
        super().__init__()
        self.signals = WorkerSignals()
        self.is_killed = False

        os.system("sudo ifconfig can0 down")
        os.system("sudo ip link set can0 type can bitrate 1000000")
        os.system("sudo ifconfig can0 txqueuelen 65536")
        os.system("sudo ifconfig can0 up")
        self.can0 = can.interface.Bus(
            channel="can0", bustype="socketcan_ctypes"
        )

    @pyqtSlot()
    def run(self) -> None:
        def parse_gear(msg: int) -> str:
            if msg == 2:
                return "N"
            elif msg > 2:
                return str(msg - 1)
            return "0"

        i = 0

        while True:
            msg = self.can0.recv(0.01)
            if msg is not None:
                self.signals.result.emit(
                    ["gear", parse_gear(int(msg.data[0]))]
                )

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

    # zatrzymanie wątku
    def kill(self) -> None:
        self.is_killed = True
