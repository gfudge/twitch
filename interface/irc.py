import socket 
import sys

class Irc:

	def __init__(self, host, port, nick, ident, realname, max_bytes=1024):
		self.socket = socket.socket()
		self.max_bytes = max_bytes
		self.host = host
		self.port = port
		self.nick = nick
		self.ident = ident
		self.realname = realname
		self.readbuffer = []
		self.start()
		
	def connect(self):
		self.socket.connect((self.host,self.port))
		self.socket.send("NICK %s\r\n" % nick)
		self.socket.send("USER %s %s bla :%s\r\n" % (ident, host, realname))
		
	def readline(self):
		self.readbuffer = self.readbuffer + self.socket.recv(1024).splitlines()	
		yield self.readbuffer.pop(0)

	def readline2(self):
		chunks = []
		bytes_recv = 0
		while bytes_recv < self.max_bytes:
			chunk = self.socket.recv()
			if chunk == '':
				raise RuntimeError("Socket broken")
			chunks.append(chunk)
			bytes_recv = bytes_recv + len(chunk)
		return ''.join(chunks)

	def start(self):
		self.connect()
		
