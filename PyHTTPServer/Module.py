from .Response import Response

class Module():
    def __init__(self, *args):
        self.load(*args)
    
    def load(self, *args):
        pass

    def __call__(self, client, request):
        return self.onexecute(client, request)

    def onexecute(self, client, request):
        res = Response.plain("Hello World")

        return res


class StaticFileModule(Module):
    def load(self, filename):
        self.filename = filename
    
    def onexecute(self, client, request):
        with open(self.filename, "rb") as file:
            data = file.read()
        
        data = data.decode("UTF-8")
        res = Response.plain(data)

        return res

class ErrorModule(Module):
    def load(self, *args):
        self.error = [500, "Internal Server Error", "Internal Server Error"]

    def onexecute(self, client, request):
        res = Response.plain(self.error[1])
        res.status[1] = self.error[0]
        res.status[2] = self.error[1]

        return res


class Error404Module(ErrorModule):
    def load(self, *args):
        self.error = [404, "Not Found", "Not Found"]