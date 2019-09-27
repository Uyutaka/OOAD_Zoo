from abc import ABCMeta, abstractmethod
from Animal import Animal

class Feline(Animal, metaclass=ABCMeta):
	@abstractmethod
	def __init__(self, name):
		super().__init__(name)

	def _roam(self):
		return super()._getName() +  "is roaming (Feline)"