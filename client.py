#!/usr/bin/python3
# Script for sending output to {internet, ink}.ed.ntnu.no
import socket
import sys
import os
import logging

log = logging.getLogger(__name__)

def send(host,data):
	#s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
	#port = 64000
	#s.connect((host, port, 0, 0))
	#s.send(bytes(data,'utf-8'))
	#s.close()
	params = data.split(' ')
	curl_command = '"curl http://%s:1515/sm/random?path=%s" > /dev/null 2>&1' % (host, params[1])
	#curl_command = "curl http://%s:1515/sm/random?path=%s" % (host, params[1])
	os.system(curl_command);
	

if __name__ == "__main__":
	if (sys.argv[1] == '--help'):
		print('usage: <server> <script> <options>)')
		exit(0)
	data = ''
	for i in range(2, len(sys.argv)):
		data = data + sys.argv[i] + ' '
	send(sys.argv[1], data)

