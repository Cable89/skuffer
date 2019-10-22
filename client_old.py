#!/usr/bin/python3
# Script for sending output to ink.ed.ntnu.no

import socket
import sys

def send(host,data):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 64000
	s.connect((host, port))
	s.send(bytes(data,'utf-8'))
	s.close()

if __name__ == "__main__":
	if (sys.argv[1] == '--help'):
		print('usage: <server> <script> <options>)')
		exit(0)
	data = ''
	for i in range(2, len(sys.argv)):
		data += sys.argv[i]
		if ( i != (len(sys.argv)-1) ):
			data += ' '
	send(sys.argv[1], data)

