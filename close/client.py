#! /usr/bin/python
# Script for sending output to ink.ed.ntnu.no

import socket
import sys

def send(host,data):
	s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
	port = 64000
	s.connect((host, port, 0, 0))
	s.send(data)
	s.close()

if __name__ == "__main__":
	if (sys.argv[1] == '--help'):
		print('usage: <server> <script> <options>)')
		exit(0)
	data = ''
	for i in range(2, len(sys.argv)):
		data = data + sys.argv[i] + ' '
	send(sys.argv[1], data)

