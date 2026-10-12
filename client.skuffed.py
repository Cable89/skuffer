#!/usr/bin/python3
# Script for sending output to {internet, ink}.ed.ntnu.no
import socket
import sys
import os

def sendd(host,data):
	s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
	port = 64000
	s.connect((host, port, 0, 0))
	s.send(bytes(data,'utf-8'))
	s.close()

def send(host,data):
	cmd = "ssh {} {}".format(host,data)
	os.system(cmd)
	#ssh internet 'play_random_from_folder.py /home/medlem/flim/skuffer/open/ida'

if __name__ == "__main__":
	if (sys.argv[1] == '--help'):
		print('usage: <server> <script> <options>)')
		exit(0)
	data = ''
	for i in range(2, len(sys.argv)):
		data = data + sys.argv[i] + ' '
	send(sys.argv[1], data)

