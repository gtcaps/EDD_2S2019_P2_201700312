import threading
import socket
import select
import sys
import time
import os
import json
from methods import *

class Thread_Client:

    def __init__(self, waiting_block, blocks_list, interval=1):
        self.interval = interval
        self.waiting_block = waiting_block
        self.blocks_list = blocks_list


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
                    
                    if message == "true":
                        if self.waiting_block is not None:
                            self.blocks_list.add(self.waiting_block)
                            self.waiting_block = None
                    elif message == "false":
                        if self.waiting_block is not None:
                            self.waiting_block = None
                    else:
                        try:
                            json.loads(message)
                            verify_string = verify_json_string(message)
                            self.waiting_block = message
                            self.server.sendall(verify_string.encode("utf-8"))
                            self.server.sendall(verify_string.encode("utf-8"))
                        except:
                            pass

    def send_message(self, message):
        self.waiting_block = message
        self.server.sendall(message.encode('utf-8'))




