class StandardInputController:

	def __init__(self, stdin):
		self.stdin = stdin[1:]
		self.flags = self.getFlags()
		self.command = self.getCommand()

	def getCommand(self):
		params = []
		for c in self.stdin:
			if c[0] != '-':
				params.append(c)
		return params

	def getFlags(self):
		flags = []
		for c in self.stdin:
			if c[0] == '-':
				flags.append(c)
		return flags

	def validateCommand(self):
		if len(self.stdin) == 0:
			print("Usage:\n\tqnote [flags] [params] [values]\n\tqnote help -> for detailed help page.")
			exit()