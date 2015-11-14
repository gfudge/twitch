#!/usr/bin/python

import socket
import sys

host = "irc.freenode.net"
port = 6667

nick = "john_cena"
ident = "john_cena"
realname = "john_cena"


def connect_irc(host, port, nick, ident, realname):
	s=socket.socket()
	s.connect((host, port))
	s.send("NICK %s\r\n" % nick)
	s.send("USER %s %s bla :%s\r\n" % (ident, host, realname))

	return s

def read_irc(s):
	readbuffer = s.recv(1024)
	readbuffer = readbuffer.splitlines()
	print readbuffer
	return readbuffer

def parse_buffer(readbuffer):
	for line in readbuffer:
		tokens = line.split()
		print tokens
		#for token in tokens:
		#	print token


def main():
	socket = connect_irc(host, port, nick, ident, realname)
	while 1:
		readbuf = read_irc(socket)
		parse_buffer(readbuf)

if __name__ == "__main__":
	main()
