import os
import can

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


# komunikacja z głównym procesem
class WorkerSignals(QObject):
    error = pyqtSignal(str)
    warning = pyqtSignal(tuple)
    result = pyqtSignal(tuple)
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
        os.system("sudo python3 " + str(os.getcwd()) + "/Workers/gcd.py &")

    @pyqtSlot()
    def run(self) -> None:
        def parse_gear(msg: int) -> str:
            if msg == 2:
                return "N"
            elif msg > 2:
                return str(msg - 1)
            return "0"

        def parse_little_endian_to_dec(num1, num2):
            binData = f"{num2:08b}" + f"{num1:08b}"
            return int(binData, 2)

        while True:
            msg = self.can0.recv(0.01)
            if msg is not None:
                if msg.arbitration_id == 1536:
                    self.signals.result.emit(
                        (
                            "rpm",
                            parse_little_endian_to_dec(
                                msg.data[0], msg.data[1]
                            ),
                        )
                    )
                    self.signals.result.emit(
                        ("air_intake_temp", int(msg.data[3]))
                    )
                elif msg.arbitration_id == 1538:
                    self.signals.result.emit(("water_temp", int(msg.data[6])))
                    self.signals.result.emit(
                        ("oil_temp", msg.data[4] * 0.0625)
                    )
                elif msg.arbitration_id == 1540:
                    self.signals.result.emit(
                        (
                            "voltage",
                            parse_little_endian_to_dec(
                                msg.data[2], msg.data[3]
                            )
                            * 0.027,
                        )
                    )
                elif msg.arbitration_id == 1:
                    self.signals.result.emit(
                        ("gear", parse_gear(int(msg.data[0])))
                    )
                    self.signals.result.emit(("gear_status", int(msg.data[1])))

            if self.is_killed:
                return

    # zatrzymanie wątku
    def kill(self) -> None:
        self.is_killed = True
