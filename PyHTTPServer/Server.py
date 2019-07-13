import socket
import ssl
import _thread
from .ClientHandler import ClientHandler
from .ModuleManager import ModuleManager

class Server():
    def __init__(self, port=8080, host="0.0.0.0", ssl=False, ssl_pem="", ssl_key=""):
        self.ssl = ssl
        self.port = port
        self.host = host
        self.ssl_pem = ssl_pem
        self.ssl_key = ssl_key
        self.clientHandler = ClientHandler(self)
        self.moduleManager = ModuleManager(self)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

        if ssl:
            if ssl_pem == "":
                Exception("Please provide a ssl_pem file!")
            if ssl_key == "":
                Exception("Please provide a ssl_key file!")
            
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(self.ssl_pem, self.ssl_key)

            self.socket = context.wrap_socket(self.sock, server_side=True)
        else:
            self.socket = self.sock

    def start(self):
        _thread.start_new_thread(self.accept_loop, ())

    def accept_loop(self):
        while True:
            conn, addr = self.socket.accept()
            _thread.start_new_thread(self.clientHandler.handle, (conn, addr))
    
    def send(self, client, packet):
        client.send(str(packet).encode("UTF-8"))
    
    def stop(self):
        self.socket.close()