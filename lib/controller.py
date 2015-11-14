import requests

class Controller():
	
	def __init__(self, hostname, command_list=None):
		self.hostname = hostname
		if command_list == None:
			self.commands = {	'forward'	: 'F',
						'backward' 	: 'B',
						'left'		: 'L',
						'right'		: 'R',
						'function_1'	: 'f1',
						'function_2'	: 'f2'};
		else:
			self.commands = command_list				

	def send(self, command):
		if command in self.commands.keys():
			requests.get(hostname + "/" + self.commands['command'])
		else:
			print "Send Error: Command invalid"

	def start(self):
		print "Controller Started"
		
