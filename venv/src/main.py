import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

import event_handler
import handler_queue


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    t = handler_queue.EventFilter(path)
    t.start()

    eventHandler = event_handler.FileEventHandler(t.event_queue)
    observer = Observer()
    observer.schedule(eventHandler, path, recursive=True)
    observer.start()

    logging.info(path)
    logging.info('rsyncher started')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
