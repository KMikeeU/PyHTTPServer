import re
from .Module import *

class ModuleManager():
    def __init__(self, server):
        self.server = server
        self.modules = {r"/404": Error404Module(self.server)}

    def register(self, trigger_regex, executable):
        self.modules[trigger_regex] = executable

    def trigger(self, client, request):
        module = r"/404"

        for key in self.modules:
            match = re.match(r"^" + key + r"$", request.status[1])
            if match != None:
                module = key
                break
        
        if module not in self.modules:
            Exception("Module for " + request.status[1] + " not found")

        res = self.modules[module](client, request)
        self.server.send(client, res)