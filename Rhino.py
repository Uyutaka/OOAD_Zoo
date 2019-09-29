from Pachyderm import Pachyderm


class Rhino(Pachyderm):
	def __init__(self, name):
		super().__init__(name)

	def _makeNoise(self):
		return super()._getName() + " is Mowwwwwww"