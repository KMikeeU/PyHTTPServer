from .Request import Request

class ClientHandler():
    def __init__(self, server):
        self.server = server
        self.clients = []
    
    def handle(self, client, addr):
        self.clients.append(client)
        
        headers = b""

        while True:
            headers += client.recv(16)

            if b"\r\n\r\n" in headers:
                headers = headers.split(b"\r\n\r\n")
                data = headers[1]
                headers = headers[0]
                break
        
        temp_headers = headers.split(b"\r\n")
        status = temp_headers[0]
        temp_headers = temp_headers[1:]

        headers = {}

        for header in temp_headers:
            header = header.decode("UTF-8").split(": ")
            headers[header[0]] = header[1]

        if "Content-Length" in headers and headers["Content-Length"] > 0:
            for _ in range(headers["Content-Length"]):
                data += client.recv(1)

        status = status.decode("UTF-8").split(" ")
        data = data.decode("UTF-8")

        req = Request(status, headers, data)

        self.server.moduleManager.trigger(client, req)