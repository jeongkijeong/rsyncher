import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

import event_handler
import handler_queue


if __name__ == "__main__":
    dirPath = sys.argv[1] if len(sys.argv) > 1 else '.'
    logFile = sys.argv[2]

    logging.basicConfig(filename=logFile, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    t = handler_queue.EventFilter(dirPath)
    t.start()

    eventHandler = event_handler.FileEventHandler(t.event_queue, logging)
    observer = Observer()
    observer.schedule(eventHandler, dirPath, recursive=True)
    observer.start()

    logging.info(dirPath)
    logging.info('rsyncher started')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
