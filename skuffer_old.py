#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import copy
import subprocess
import threading
GPIO.setmode(GPIO.BOARD)

maxThreads = 10

skuffer =  []
skuffer_prev = []
reol = []
skuff = [1,0]		#[RPI Pin no, skuff status
for i in range(0,4):
	reol.append(copy.deepcopy(skuff))
for i in range(0,12):
	skuffer.append(copy.deepcopy(reol))

#for i in range(0,12):
#	for j in range(0,4):
#		print("Skuff: ",i,j,skuffer[i][j])


skuffer[6][0][0] = 31	# Arne
skuffer[6][1][0] = 33	# Kabbe
skuffer[6][2][0] = 35	# Stig
skuffer[6][3][0] = 37	# Charlotte

skuffer[7][0][0] = 8	# Vlad
skuffer[7][1][0] = 10	# Torgeir
skuffer[7][2][0] = 12	# LB1DG
skuffer[7][3][0] = 16	# Frode

skuffer[8][0][0] = 7	# Gustav
skuffer[8][1][0] = 11	# Loverboy
skuffer[8][2][0] = 13	# Torbjorn
skuffer[8][3][0] = 15	# Mini Are

skuffer[11][0][0] = 18	# Super
skuffer[11][1][0] = 22	# Laurits
skuffer[11][2][0] = 26	# Arild
skuffer[11][3][0] = 32	# Mekaa



def skuffOpened(reol, skuff):
	script = "/home/medlem/skuffer/open/R" + str(reol) + "S" + str(skuff) + ".py"
	print ("Reol: " + str(reol) + " Skuff: " + str(skuff) + " Opened")
	try:
		subprocess.call([script])
	except:
		print ("Script" + script + " not found")

def skuffClosed(reol, skuff):
	script = "/home/medlem/skuffer/close/R" + str(reol) + "S" + str(skuff) + ".py"
	print ("Reol: " + str(reol) + " Skuff: " + str(skuff) + " Closed")
	try:
		subprocess.call([script])
	except:
		print ("Script" + script + " not found")

#for i in range(1,41):
for reol in range(0,12):
	for skuff in range(0,4):
		try:
			print(skuffer[reol][skuff][0])
			GPIO.setup(skuffer[reol][skuff][0],GPIO.IN,pull_up_down=GPIO.PUD_UP)
		except:
			print("wololo")
			#pass

for reol in range(0,12):
	for skuff in range(0,4):
		try:
			skuffer[reol][skuff][1] = GPIO.input(skuffer[reol][skuff][0])
		except:
			pass

skuffer_prev =  copy.deepcopy(skuffer)


while True:
	#for i in range(1,41):
	#	try:
	#		print("Pin ",i," : ", GPIO.input(i))
	#	except:
	#		pass
	#sleep(1)
	#print(" ")
	
	skuffer_prev =  copy.deepcopy(skuffer)
	
	for reol in range(0,12):
		for skuff in range(0,4):
			try:
				skuffer[reol][skuff][1] = GPIO.input(skuffer[reol][skuff][0])
			except:
				pass
			
			if skuffer[reol][skuff][1] != skuffer_prev[reol][skuff][1]:
				if skuffer[reol][skuff][1] == 1:
					#print("Skuff",reol, skuff, "Aapnet")
					if (threading.activeCount() < maxThreads):
						w = threading.Thread(target=skuffOpened,args=(reol, skuff,))
						w.start()
				else:
					#print("Skuff",reol, skuff, "Lukket")
					if (threading.activeCount() < maxThreads):
						w = threading.Thread(target=skuffClosed,args=(reol, skuff,))
						w.start()
	sleep(1)




