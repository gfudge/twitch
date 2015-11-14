#!/usr/bin/python

import socket
import sys

#sys.path.append('lib')

from lib.irc import Irc
from lib.controller import Controller

device_ip = "192.168.0.2"
device_port = 80

twitch_host = "irc.freenode.net"
twitch_port = 6667

nick = "john_cena"
ident = "john_cena"
realname = "john_cena"

command_list = {'forward' 	: 'F',
		'backward' 	: 'B',
		'left'		: 'L',
		'right'		: 'R',
		'function1'	: 'f1',
		'function2'	: 'f2'
		};

command_filter = command_list.items()

def filter(irc, controller, filter):
	#for line in irc.readline():
		
	words = ["".join([x for x in t.split() if not x in command_filter]) for t in irc.readline()]

def main():
	irc = Irc(twitch_host, twitch_port, nick, ident, realname)
	controller = Controller(device_ip)
	

if __name__ == "__main__":
	main()
