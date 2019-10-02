'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Hippo.py

@Time    :   09/28/2019

@Desc    :   This class is a concrete hippo class, it implements the _makeNoise() function.

'''

from Pachyderm import Pachyderm


class Hippo(Pachyderm):
	def __init__(self, name):
		super().__init__(name)

	def _makeNoise(self):
		return super()._getName() + " is Mowww"