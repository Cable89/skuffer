#! /usr/bin/python3
# script for reading inputs

import subprocess
import threading
import serial
import copy
import time
import sys

pinmap0 = {
	'P2'		:'R0S0',
	'P3'		:'R0S1',
	'P4'		:'R0S2',
	'P5'		:'R0S3',
	'P6'		:'R1S0',
	'P7'		:'R1S1',
	'P8'		:'R1S2',
	'P9'		:'R1S3',
	'P10'		:'R2S0',
	'P16'		:'R2S1',
	'P14'		:'R2S2',
	'P15'		:'R2S3',
	'A0'		:'R3S0',
	'A1'		:'R3S1',
	'A2'		:'R3S2',
	'A3'		:'R3S3',
}

pinmap1 = {
	'P6'		:'R4S0',
	'P7'		:'R4S1',
	'P8'		:'R4S2',
	'P9'		:'R4S3',
	'P2'		:'R5S0',
	'P3'		:'R5S1',
	'P4'		:'R5S2',
	'P5'		:'R5S3',
	'A0'		:'R6S0',
	'A1'		:'R6S1',
	'A2'		:'R6S2',
	'A3'		:'R6S3',
	'P10'		:'R7S0',
	'P16'		:'R7S1',
	'P14'		:'R7S2',
	'P15'		:'R7S3',
}

pinmap2 = {
	'P6'		:'R8S0',
	'P7'		:'R8S1',
	'P8'		:'R8S2',
	'P9'		:'R8S3',
	'P2'		:'R9S0',
	'P3'		:'R9S1',
	'P4'		:'R9S2',
	'P5'		:'R9S3',
	'A0'		:'R10S0',
	'A1'		:'R10S1',
	'A2'		:'R10S2',
	'A3'		:'R10S3',
	'P10'		:'R11S0',
	'P16'		:'R11S1',
	'P14'		:'R11S2',
	'P15'		:'R11S3',
}

def main():
	w0 = threading.Thread(target=readFromGPIOExtender,args=('/dev/ttyIO0',pinmap0))
	w1 = threading.Thread(target=readFromGPIOExtender,args=('/dev/ttyIO1',pinmap1))
	w2 = threading.Thread(target=readFromGPIOExtender,args=('/dev/ttyIO2',pinmap2))
	w0.start()
	w1.start()
	w2.start()

def readFromGPIOExtender(device,extended_pins):
	print("readFromGPIOExtender")
	ser = serial.Serial(device,9600, timeout=0.4)
	ser.flush()
	
	while True:
		try:
			serialinput = ser.readline().decode('utf-8')
			button = serialinput.split(':')
			if(button[1][0] == '1'):
				buttonPress(extended_pins[(button[0])])
			else:
				buttonRelease(extended_pins[(button[0])])
		except:
			time.sleep(0.1)		



def buttonPress(button):
	script = "/home/medlem/skuffer/close/" + button + ".py"
	print("Skuff closed " + button)
	try:
		subprocess.Popen([script])
	except:
		print("Script " + script + " not found")

def buttonRelease(button):
	print("Skuff opened " + button)
	script = "/home/medlem/skuffer/open/" + button + ".py"
	try:
		subprocess.Popen([script])
	except:
		print("Script " + script + " not found")


main()
