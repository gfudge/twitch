#!/usr/bin/python

import socket
import sys

from interface import irc
from interface import interface

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

def main():
	irc = Irc(twitch_host, twitch_port, nick, ident, realname)
	controller = Controller(device_ip)
	

if __name__ == "__main__":
	main()
