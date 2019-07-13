from .Packet import Packet

class Response(Packet):
    @staticmethod
    def plain(text):
        self = Response(["HTTP/1.1", "200", "OK"], {
            "Connection": "close",
            "Content-Type": "text/html"
        }, text)
        
        return self
    
    def prepare(self):
        if "Server" not in self.headers:
            self.headers["Server"] = "PyHTTPServer"