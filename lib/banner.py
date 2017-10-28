#!/usr/bin/python

from lib.constants import VERSION, TC


srvbanner = """

""" + TC.END + TC.BOLD + "    TCP Reverse Shell - Server" + """
    [Version %s] """ % (VERSION) + """
    @a7kemc73

""" + TC.END


clibanner = """

""" + TC.END + TC.BOLD + "    TCP Reverse Shell - Client" + """
    [Version %s] """ % (VERSION) + """
    @a7kemc73

""" + TC.END


srvusage = TC.END + """

    ./tcpsrv.py [OPTIONS]

"""


cliusage = TC.END + """

    ./tcpcli.py [OPTIONS]

"""
