#class for items

class Item:
	
	def __init__(self, name, description, parent):
		self.name = name
		self.description = description
		self.parent = parent

	def getName(self):
		return self.name
	def setName(self, newName):
		self.name = newName

	def getDesc(self):
		return self.description
	def setDesc(self, newDesc):
		self.description = newDesc

	def getParent(self):
		return self.parent
	def setParent(self, newParent):
		self.parent = newParent
