#!/usr/bin/python

from lib.constants import TC


#
#
#
def print_error(error):
	print TC.RED + TC.BOLD + "[X] " + TC.END + TC.RED + error + TC.END


#
#
#
def print_warning(warning):
	print TC.YELLOW + TC.BOLD + "[!] " + TC.END + TC.YELLOW + warning + TC.END


#
#
#
def print_success(success):
	print TC.GREEN + TC.BOLD + "[+] " + TC.END + TC.GREEN + success + TC.END


#
#
#
def print_info(info):
	print TC.BLUE + TC.BOLD + "[-] " + TC.END + TC.BLUE + info + TC.END


#
#
#
def prompt(text):
	thePrompt = TC.CYAN + text + ">> " + TC.END
	return thePrompt
