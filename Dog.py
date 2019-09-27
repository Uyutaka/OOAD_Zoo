from Canine import Canine

class Dog(Canine):
	def __init__(self, name):
		super().__init__(name)
	def _makeNoise(self):
		return super()._getName() + " is Wang Wang"