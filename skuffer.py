#!/usr/bin/python3
# script for reading inputs

import subprocess
import threading
import serial
import copy
import time
import sys
from pathlib import Path
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

pinmap3 = {
        'K1'            :'R12S1',
        'K2'            :'R13S3',
        'K3'            :'R13S0',
        'K4'            :'R13S2',
        'K5'            :'R12S2',
        'K6'            :'R12S3',
        'K7'            :'R13S1',
        'K8'            :'R12S0',
	'K9'            :'R-1S3',
        'K10'            :'R-1S2',
        'K11'            :'R-1S1',
        'K12'            :'R-1S0',

}

def main():
	time.sleep(5) #wait for all devices to come online/power on (specifically fixing the arduino/ttyUSB0)
	w0 = threading.Thread(target=readFromGPIOExtender,args=('/dev/ttyACM0',pinmap0))
	w1 = threading.Thread(target=readFromGPIOExtender,args=('/dev/ttyACM1',pinmap1))
	w2 = threading.Thread(target=readFromGPIOExtender,args=('/dev/ttyACM3',pinmap2))

	a = Path("/dev/ttyUSB0")
	if a.exists():
		w3 = threading.Thread(target=readFromGPIOExtender,args=('/dev/ttyUSB0',pinmap3))
	else:
		w3 = threading.Thread(target=readFromGPIOExtender,args=('/dev/ttyUSB1',pinmap3))
	w0.start()
	w1.start()
	w2.start()
	w3.start()

def readFromGPIOExtender(device,extended_pins):
	print("readFromGPIOExtender")
	ser = serial.Serial(device,9600, timeout=0.4)
	ser.flush()
	
	while True:
		try:
			serialinput = ser.readline().decode('utf-8')
			button = serialinput.split(':')
			if(len(button) > 1):
				if(len(button[1]) > 0):
					print("read " + serialinput)
					if(button[1][0] == '1'):
						print("I stopped closing sounds")
						#buttonPress(extended_pins[(button[0])])
					else:
						buttonRelease(extended_pins[(button[0])])
		except:
			time.sleep(0.1)		



def buttonPress(button):
	script = "/home/medlem/skuffer/close/" + button + ".py"
	print("Skuff closed " + button)
	try:
		subprocess.Popen(['python3',script])
	except:
		print("Script " + script + " not found")

def buttonRelease(button):
	print("Skuff opened " + button)
	script = "/home/medlem/skuffer/open/" + button + ".py"
	try:
		subprocess.Popen(['python3',script])
	except:
		print("Script " + script + " not found")


main()
