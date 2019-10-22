#!/usr/bin/python

import client
import can
from time import sleep

#allow only one intance of program
from tendo import singleton
me = singleton.SingleInstance() # will sys.exit(-1) if other instance is running

#client.send("internet","kjabbewrap.py /home/medlem/flim/juice.mkv")
client.send("internet","kjabbewrap.py /media/nfs/ovsky/OVSky/divskrot/flim/worst.webm")

#software debounce
sleep(3)
#client.send("internet","kjabbewrap.py /home/medlem/flim/gas_gas_gas_cut.mkv")
#can.pingpong()
