import os
from save import Save
from win10toast import ToastNotifier
import inotify.adapters

toaster = ToastNotifier()

home = os.path.expanduser('~')
location = os.path.join(home, 'Downloads')
folder_check = os.path.isdir(location)
if folder_check == False:
    quit("no downloads folder")

notifier = inotify.adapters.Inotify()
notifier.add_watch(location)

f = open("./assignments.lb2", "r")
saves = []
for line in f:
    args = line.split()
    saves.append(Save(args[0], args[1:]))


for event in notifier.event_gen(yield_nones=False):
    (_, type_names, path, filename) = event

    print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
        path, filename, type_names))
