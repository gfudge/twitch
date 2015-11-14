import socket 
import sys

class irc:

	def __init__(self, host, port, max_bytes=100):
		self.irc = socket.socket()
		self.max_bytes = max_bytes
		self.host = host
		self.port = port
	
	def connect(self):
		self.irc.connect((self.host,self.port))
	
	def readline(self):
		chunks = []
		bytes_recv = 0
		while bytes_recv < self.max_bytes:
			chunk = self.irc.recv()
			if chunk == '':
				raise RuntimeError("Socket broken")
			chunks.append(chunk)
			bytes_recv = bytes_recv + len(chunk)
		return ''.join(chunks)
