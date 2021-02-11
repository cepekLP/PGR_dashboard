import time
import socket

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


class Server(QRunnable):
    def __init__(self):
        super().__init__()
        self.info = ""
        self.extended_info = ""


    @pyqtSlot()
    def run(self):
        serverSocket = socket.socket()  
        host = '' 
        port = 8080 
        serverSocket.bind( ( host, port ) )  
        serverSocket.listen( 1 )  
        
        while True:
            con, addr = serverSocket.accept() 
            con.settimeout(15)
            
            while True:  
                try:
                    con.send( self.info )  
                                      
                    message = con.recv( 1024 ).decode( "utf-8" )  
                except:
                    break
  
                time.sleep( 0.25 )  

            con.close()                 
            

    def update(self, bolide_info):
        self.info = bytes(str(bolide_info.__dict__),"utf-8")


    #zatrzymanie wątku
    def kill(self):
        self.is_killed = True


        





