#!/usr/bin/python

import client
import random
r = random.randint(0,2)
if r==1:
	client.send("internet","kjabbewrap.py /media/nfs/ovsky/OVSky/Brukere/Andreas/skuff/shrek.mp4")
else:
	client.send("internet","kjabbewrap.py /media/nfs/ovsky/OVSky/Brukere/Andreas/skuff/johny.mp4")
