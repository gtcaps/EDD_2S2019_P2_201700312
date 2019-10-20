import threading
import socket
import select
import sys
import time
import os

class Thread_Client:

    def __init__(self, interval=1):
        self.interval = interval

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if len(sys.argv) != 3:
	        print ("Correct usage: script, IP address, port number")
	        exit()
        IP_address = str(sys.argv[1])
        Port = int(sys.argv[2])
        self.server.connect((IP_address, Port))

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()


    def run(self):
        while True:
            read_sockets = select.select([self.server], [], [], 1)[0]
            for socks in read_sockets:
                if socks == self.server:
                    message = socks.recv(2048)
                    message = str(message.decode('utf-8'))
                    message = message.strip()
                    
                    #print (message.decode('utf-8'))
                    if message == "true":
                        print("Voy a añadir el bloque a la lista de blockchains")
                    elif message == "false":
                        print("No puedo añadir el bloque a la lista, porque fue modificado")
                    else:
                        pass
                        #print("Voy a verificar la cadena que me has enviado y procesar el json:----->{}<------------".format(message))
            time.sleep(self.interval)

    def send_message(self, message):
        self.server.sendall(message.encode('utf-8'))




