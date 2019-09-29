from Pachyderm import Pachyderm


class Elephant(Pachyderm):
	def __init__(self, name):
		super().__init__(name)

	def _makeNoise(self):
		return super()._getName() + " is WYuuuuu"