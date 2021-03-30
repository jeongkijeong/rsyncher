import os
import handler_queue
from watchdog.events import LoggingEventHandler


class FileEventHandler(LoggingEventHandler):
    queue = None

    def __init__(self, queue):
        self.queue = queue

    def on_created(self, event):
        self.send(event)

    def on_modified(self, event):
        self.send(event)

    def on_deleted(self, event):
        self.send(event)

    def send(self, event):
        self.queue.put(event)
