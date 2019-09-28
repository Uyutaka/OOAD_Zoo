from Canine import Canine


class Dog(Canine):
	def __init__(self, name, makeNoise):
		super().__init__(name)
		self.makeNoise = makeNoise

	def _makeNoise(self):
		return super()._getName() + self.makeNoise.makeNoise()