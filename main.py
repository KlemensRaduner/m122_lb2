import os
import threading
from win10toast import ToastNotifier
from infi.systray import SysTrayIcon


class Save:  # stores the assignments of directory to filextensions
    def __init__(self, dir, extensions):
        self.dir = dir
        self.extensions = extensions

    def hasExtension(self, e):
        return e in self.extensions


# initalize toaster
toaster = ToastNotifier()

# get path to download folder
home = os.path.expanduser('~')
location = os.path.join(home, 'Downloads')
folder_check = os.path.isdir(location)
if folder_check == False:  # exit if downloads folder does not exist
    quit("no downloads folder")

# read file with the assignments and store them in "saves"
f = open("./assignments.txt", "r")
saves = []
for line in f:
    args = line.split()
    saves.append(Save(args[0], args[1:]))


def moveFiles():  # moves files
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
    # show toast if any files moved
    if moved:
        toaster.show_toast("LB2", str(moved) +
                           "files moved", icon_path="icon.ico", duration=5,
                           threaded=True)


# run programm
moveFiles()


def edit_options(systray):  # edit options
    os.system("notepad.exe assignments.txt")


def on_quit_callback(systray):  # quit
    exit()


# adding menuoptions to systray
menu_options = (("Edit options", None, edit_options),)

systray = SysTrayIcon("icon.ico", "File mover",
                      menu_options, on_quit=on_quit_callback)
systray.start()
