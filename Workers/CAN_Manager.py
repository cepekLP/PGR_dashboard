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

        def parse(num1, num2):
            binData = f"{num2:08b}" + f"{num1:08b}"
            return int(binData, 2)

        while True:
            msg = self.can0.recv(0.01)
            if msg is not None:
                if msg.arbitration_id == 1536:
                    self.signals.result.emit(
                        (
                            "rpm",
                            parse(msg.data[0], msg.data[1]),
                        )
                    )
                    self.signals.result.emit("TPS", int(msg.data[2]) * 0.5)
                    self.signals.result.emit(
                        ("air_intake_temp", int(msg.data[3]))
                    )
                    self.signals.result.emit("MAP", int(msg.data[4]))
                elif msg.arbitration_id == 1538:
                    self.signals.result.emit(("water_temp", int(msg.data[6])))
                    self.signals.result.emit(
                        ("oil_temp", round(msg.data[4] * 0.0625, 2))
                    )
                elif msg.arbitration_id == 1539:
                    self.signals.result.emit(
                        ("lambda", round(int(msg.data[3]) * 0.0078125, 2))
                    )
                elif msg.arbitration_id == 1540:
                    self.signals.result.emit(("ecu_temp", int(msg.data[1])))
                    self.signals.result.emit(
                        (
                            "voltage",
                            round(parse(msg.data[2], msg.data[3]) * 0.027, 2),
                        )
                    )
                    self.signals.result.emit("gear_cut", int(msg.data[6]))
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
