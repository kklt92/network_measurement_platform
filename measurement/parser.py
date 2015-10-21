#!/usr/bin/python

from .command import Command
import re
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
    m = None
    for line in f:
        line_arr = line.strip().split()
        if len(line_arr) == 0: 
            continue
        line = re.sub(r'#.*$', '', line) # ignore comment
        value = re.findall(r"['\"](.*?)['\"]", line)

        if line_arr[0] == "service":
            if m:
                mq.ready_queue.append(m)
            m = Measurement(line_arr[1])
        elif line_arr[0] == "option":
            m.parse(line_arr[1], value[0])
        else:
            print "Unsupported arguments: " + line
    if m:
        mq.ready_queue.append(m)


class Measurement:
    """a measurement class"""

    def __init__(self, name):
        self.name = name
        self.cmd = Command()
        self.report = None

    def parse(self, option, val):
        key = option
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


