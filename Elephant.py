'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Elephant.py

@Time    :   09/28/2019

@Desc    :   This class is a concrete Elephant class, it implements the _makeNoise() function.

'''

from Pachyderm import Pachyderm


class Elephant(Pachyderm):
	def __init__(self, name):
		super().__init__(name)

	def _makeNoise(self):
		return super()._getName() + " is WYuuuuu"