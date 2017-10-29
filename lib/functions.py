#!/usr/bin/python

from lib.constants import TC
import sys


#
#
#
def print_error(error):
	sys.stdout.write(TC.RED + TC.BOLD + "[X] " + TC.END + TC.RED + error + TC.END)


#
#
#
def print_warning(warning):
	sys.stdout.write(TC.YELLOW + TC.BOLD + "[!] " + TC.END + TC.YELLOW + warning + TC.END)


#
#
#
def print_success(success):
	sys.stdout.write(TC.GREEN + TC.BOLD + "[+] " + TC.END + TC.GREEN + success + TC.END)


#
#
#
def print_info(info):
	sys.stdout.write(TC.BLUE + TC.BOLD + "[-] " + TC.END + TC.BLUE + info + TC.END)


#
#
#
def print_progress(text):
	sys.stdout.write(TC.BLUE + text + TC.END)


#
#
#
def prompt(text):
	thePrompt = TC.CYAN + text + ">> " + TC.END
	return thePrompt
