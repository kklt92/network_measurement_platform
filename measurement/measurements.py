import time
import thread
from subprocess import Popen, PIPE, call
from urllib2 import Request, urlopen, URLError

def exec_experiment(thread_name, rqueue, cqueue):
    while True:
        while len(rqueue) == 0:
            time.sleep(1)
        m = rqueue.pop(0)
        print m.cmd.cmd
        #call(m.cmd.cmd, stdout=m.report)
        p = Popen(m.cmd.cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        m.report = p.communicate()
        cqueue.append(m)

    
def get_query_url(base_url): 
    # TODO construct url by local machine parameters
    ret = base_url
    return ret


class Measurements:
    def __init__(self):
        self.ready_queue = []           # TODO adding to file, need to be store and will not be lost if restart machine.
        self.completed_queue = []
        self.query_server_url = "http://api.example.com"  # TODO change to be query server
        self.query_server_url = "127.0.0.1:5000"  # TODO change to be query server
        
        try:
            # TODO thread.start_new_thread(query)
            thread.start_new_thread(query_instruction)
            thread.start_new_thread(exec_experiment, ("experiment", self.ready_queue, self.completed_queue))
            # TODO thread.start_new_thread(report)
        except:
            print "Error: Unable to start thread"

    def query_instruction(self):
        request = Request(get_query_url(self.query_server_url))
        try:
            response = urlopen(report).read()
            print response
        except URLError, e:
            print 'Error: ', e
            
    def send_report(self):
        while len(self.completed_queue) > 0:
            curr = self.completed_queue.pop()
