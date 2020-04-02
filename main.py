import os
import threading
from win10toast import ToastNotifier


class Save:
    def __init__(self, dir, extensions):
        self.dir = dir
        self.extensions = extensions

    def hasExtension(self, e):
        return e in self.extensions


toaster = ToastNotifier()
home = os.path.expanduser('~')
location = os.path.join(home, 'Downloads')
folder_check = os.path.isdir(location)
if folder_check == False:
    quit("no downloads folder")

f = open("./assignments.lb2", "r")
saves = []
for line in f:
    args = line.split()
    saves.append(Save(args[0], args[1:]))


def moveFiles():
    threading.Timer(1.0, moveFiles).start()
    files = os.listdir(location)
    moved = 0
    for file in files:
        name, extension = os.path.splitext(file)
        for save in saves:
            if save.hasExtension(extension):
                os.rename(os.path.join(location, file),
                          os.path.join(save.dir, name+extension))
                moved += 1
    if moved:
        toaster.show_toast("LB2", str(moved) + " files moved")


moveFiles()
