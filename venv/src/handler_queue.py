import threading
import queue
import rsync_handler

# host, target server IP, target server path, passowrd
target_list = [
     ["admin", "192.168.128.85", "/home/tmp", "mypassword"],
    ]


class EventFilter(threading.Thread):
    event_queue = queue.Queue()
    event_occur = False

    def __init__(self, param):
        super(EventFilter, self).__init__()
        self.myPath = param

    def run(self):
        while True:
            try:
                self.event_queue.get(block=True, timeout=5)
                self.event_occur = True
            except Exception as e:
                self.process()
                self.event_occur = False

    def process(self):
        if self.event_occur is True:
            for target in target_list:
                password = target[3]

                # source_path = '/data/home/ubotapp/tmp'
                source_path = self.myPath
                target_path = '%s@%s:%s' % (target[0], target[1], target[2])

                rsync_handler.call_rsync(source_path, target_path, password)
