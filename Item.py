#class for items

class Item:
	
	def __init__(self, name, description, parent):
		self.name = name
		self.description = description
		self.parent = parent

	def getName():
		return self.name
	def setName(newName):
		self.name = newName

	def getDesc():
		return self.description
	def setDesc(newDesc):
		self.description = newDesc

	def getParent():
		return self.parent
	def setParent(newParent):
		self.parent = newParent
