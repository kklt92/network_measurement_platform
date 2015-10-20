import platform

class Command:
    def __init__(self):
        self.cmd = []
        self.system = platform.system().lower()

    def add_method(self, method):
        if self.system == "linux":
            if method.lower() == "ping":
                self.cmd.insert(0, "ping")
                self.method = "ping"
    def add_arg(self, arg):
        if(self.method == "ping"):
            if(arg[0] == "count"):
                self.cmd.append("-c" + arg[1])
            if(arg[0] == "ttl"):
                self.cmd.append("-t" + arg[1])
            if(arg[0] == "packetsize"):
                self.cmd.append("-s" + arg[1])
    def add_dest(self, dest):
        self.cmd.append(dest)





