import time
import socket

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot, QThread

COMMAND = 64
VALUE = 64


class WorkerSignals(QObject):
    warning = pyqtSignal(list)


class Server(QRunnable):
    info = ""
    extended_info = ""
    time_sleep = 0.25
    is_killed = False

    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        serverSocket = socket.socket()  
        host = '' 
        port = 8080 
        serverSocket.bind((host, port))  
        serverSocket.listen(1)  
        
        while not self.is_killed:
            con, addr = serverSocket.accept() 
            con.settimeout(15)
            
            while True:  
                try:
                    con.send(self.info)                                        
                    message = con.recv(COMMAND).decode("utf-8")  
                except:
                    break

                message = message.translate({ord(' '): None})
                if message == "OK": 
                    pass
                else:
                    value = con.recv(VALUE).decode("utf-8")
                    if message == "TIME":
                        self.time_sleep = float(value)
                    elif message == "INFO":
                        self.signals.warning.emit([message.lower(), value])

                time.sleep(self.time_sleep)  

            con.close()                 
            

    def update(self, bolide_info):
        self.info = bytes(str(bolide_info),"utf-8")


    #zatrzymanie wątku
    def kill(self):
        self.is_killed = True


        




