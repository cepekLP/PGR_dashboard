import time
import socket

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

BUFFER_SIZE = 32

class Server(QRunnable):
    def __init__(self):
        super().__init__()
        self.info = ""
        self.extended_info = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((socket.gethostname(), 8080))
        self.sock.listen(1)


    @pyqtSlot()
    def run(self):
        i = 0
        #test połączenia
        
        while True:
            cs, addr = self.sock.accept()
            print('Connection address:', addr)
            while 1:
                data = cs.recv(BUFFER_SIZE)
                if not data: break
  
            
                cs.send(self.info)     # echo
            cs.close()
        

    def update(self, bolide_info):
        self.info = bytes(str(bolide_info.__dict__),"utf-8")


    #zatrzymanie wątku
    def kill(self):
        self.is_killed = True


        





