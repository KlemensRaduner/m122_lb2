import os

home = os.path.expanduser('~')
location = os.path.join(home, 'Downloads')
folder_check = os.path.isdir(location)
if folder_check != True:
    quit("no downloads folder")

f = open("./assignments.lb2", "r")
line = f.readline()
args = line.split()
