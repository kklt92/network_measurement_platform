#!/usr/bin/python

"""
service "example-measurement-name"
    option method       "ping"
    option argument     "count 10"      # multi-arguments support
    option argument     "ttl 30"
    option argument     "packetsize 56"
    option destination  "8.8.8.8"
    option schedule     "10 3 1 1 *"    # cron format
    option repeat       "3"             # repeat 3 times.
"""

def file_read(f, mq):
    for line in f:
        line_arr = line.split(' ')
        if len(line_arr) == 0: 
            continue
        if line_arr[0] == "service":
            if m:
                mq.ready_queue.append(m)
            m = Measurement(line_arr[1])
        elif line_arr[0] == "option":
            m.parse(line_arr[1:])
        else:
            print "Unsupported arguments: " + line
    if m:
        mq.ready_queue.append(m)


class Measurement:
    """a measurement class"""

    def __init__(self, name):
        self.name = name
        self.cmd = Command()
        self.report = ""

    def parse(self, options):
        if(len(options) != 2):
            print "Unexpected options: " + options
            return 

        key = options[0]
        val = optinos[1]
        if key == "method":
            self.cmd.add_method(val)
        elif key == "argument":
            self.cmd.add_arg(val)
        elif key == "destination":
            self.cmd.add_dest(val)
        elif key == "schedule":
            # TODO adding multithreading threading.Timer()
            print "Schedule"
        elif key == "repeat":
            # TODO multithreading
            print "Repeat"


