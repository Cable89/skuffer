#!/usr/bin/python

import client
import os

file_path = "/home/medlem/skuffer/open/kontiki_count.txt"

try:
    os.chmod(file_path,0777)
except:
    pass

kontiki_count = 0
try:
    with open(file_path,'r') as file:
        line = file.readline()
	if len(line) and line[-1] == '\n':
            line = line[:len(line) - 1]
        kontiki_count = int(line)
except:
    pass

kontiki_count += 1
with open(file_path, 'w') as file:
    file.write(str(kontiki_count))

client.send("internet","nyskjegg.sh " + str(kontiki_count))
