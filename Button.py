#Button class

class Button(UIElement):

	def __init__(self, width, height, ParentScreen, color):
		self.width = width
		self.height = height
		self.ParentScreen = ParentScreen
		self.color = color

	def getWidth():
		return width
	def setWidth(newWidth):
		self.width = newWidth
	
	def getHeight():
		return height
	def setHeight(newHeight):
		self.height = newHeight

	def getParentScreen():
		return ParentScreen
	def setParentScreen(newParent):
		self.ParentScreen = newParent

	def getColor():
		return self.color
	def setColor(newColor):
		self.color = newColor
