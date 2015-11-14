import socket
import sys

class interface():

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.isInit = False

	def connect(self):
		self.socket = socket.socket()
		self.socket.connect((self.host, self.port))
		self.isInit = True

	def kill(self):
		self.socket.close()
		self.send("CLOSE")
		self.isInit = False

	def send(self, message):
		totalsend = 0
		while totalsend < len(message):
			sent = self.socket.send(message[totalsend:])
			totalsend = totalsend + sent
			if sent == 0:
				raise RuntimeError("Socket connection broken")

	def start(self):
		self.connect()
		self.send("INIT")

