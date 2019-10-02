'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Rhino.py

@Time    :   09/28/2019

@Desc    :   This class is a concrete Rhino class, it implements the _makeNoise() function.

'''

from Pachyderm import Pachyderm


class Rhino(Pachyderm):
	def __init__(self, name):
		super().__init__(name)

	def _makeNoise(self):
		return super()._getName() + " is Mowwwwwww"