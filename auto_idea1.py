# Moving a file from Source Folder to Destination folder
# by bernardinho.codes

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event, folder_to_track=None):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)


folder_to_crack = "/home/bernadinho/Schreibtisch/old" #Source folder
folder_destination = "/home/bernadinho/Schreibtisch/new" #Destination folder

# Creating the Observer
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_crack, recursive=True)
observer.start()



# Observer start here
try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()

