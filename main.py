import os
from save import Save

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

files = os.listdir(location)
for file in files:
    name, extension = os.path.splitext(file)
    for save in saves:
        if save.hasExtension(extension):
            os.rename(os.path.join(location, file),
                      os.path.join(save.dir, name+extension))
