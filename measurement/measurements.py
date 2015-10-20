import time
import thread
from subprocess import call

def exec_measurement(thread_name, rqueue, cqueue):
    while True:
        while len(rqueue) == 0:
            time.sleep(10)
        m = rqueue.pop(0)
        call(m.cmd.cmd, stdout=m.report)
        cqueue.append(m)

class Measurements:
    def __init__(self):
        self.ready_queue = []
        self.completed_queue = []
        try:
            # TODO thread.start_new_thread(query)
            thread.start_new_thread(exec_measurement, ("measure", self.ready_queue, self.completed_queue))
            # TODO thread.start_new_thread(report)
        except:
            print "Error: Unable to start thread"

