
class Packet():
    def __init__(self, status, headers, data):
        self.status = status
        self.headers = headers
        self.data = data

    def parse(self):
        self.prepare()
        return self.__str__()

    def __str__(self):
        s = ""
        status = [str(i) for i in self.status]
        
        s += " ".join(status)
        s += "\r\n"
        
        if "Content-Length" not in self.headers:
            self.headers["Content-Length"] = len(self.data)

        for key in self.headers:
            s += str(key) + ": " + str(self.headers[key]) + "\r\n"
        
        s += "\r\n"
        
        s += self.data

        return s
    
    def prepare(self):
        return