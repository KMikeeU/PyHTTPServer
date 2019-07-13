import PyHTTPServer

server = PyHTTPServer.Server()                                  # Creating a new HTTP server
server.start()                                                  # Starting a Server


home = PyHTTPServer.Module.StaticFileModule("example.html")       # Creating a module to be used as a Home route
server.moduleManager.register(r"/", home)                         # Loading the module


try:                                                            # Do something else ...
    while True:
        input("$> ")
except:
    server.stop()