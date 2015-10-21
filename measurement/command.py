import platform

def linux_map(x):
    return {
        "ping"          : "ping",
        "traceroute"    : "traceroute",
    }.get(x, "Error")


class Command:
    def __init__(self):
        self.cmd = []
        self.method = ""
        self.system = platform.system().lower()

    def add_method(self, method):
        self.method = method
        if self.system == "linux":
            self.cmd.insert(0, linux_map(method))
        elif self.system == 'darwin':
            self.cmd.insert(0, linux_map(method))
    def add_arg(self, arg):
        arg = arg.split()
        if(self.method == "ping"):
            if(arg[0] == "count"):
                self.cmd.append("-c " + arg[1])
            elif(arg[0] == "ttl"):
                if self.system == "linux":
                    self.cmd.append("-t " + arg[1])
                elif self.system == "darwin":
                    #TODO
                    return 

            elif(arg[0] == "packetsize"):
                self.cmd.append("-s " + arg[1])
    def add_dest(self, dest):
        self.cmd.append(dest)
