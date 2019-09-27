from Feline import Feline

class Lion(Feline):
	def __init__(self, name):
		super().__init__(name)

	def _makeNoise(self):
		return super()._getName() + " is Aoooooo"