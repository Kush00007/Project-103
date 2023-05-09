import logging
import os
import random
import shutil
import sys
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from_dir = "E:/Downloads"


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("Hey," + {event.src_path} + "has been created!")

    def on_deleted(self, event):
        print("Oops! Someone deleted" + {event.src_path} + "!")

    def on_modified(self, event):
        print("Hey there!," + {event.src_path} + "has been modified")

    def on_moved(self, event):
        print("Someone moved" + {event.src_path} + "to" + {event.dest_path})


event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
