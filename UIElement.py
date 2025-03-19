from abc import ABC, abstractmethod

class UIElement(ABC):
	@abstractmethod
	def draw():
		pass
	def move():
		pass
	def resize():
		pass
