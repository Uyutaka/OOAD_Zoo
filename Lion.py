'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Lion.py

@Time    :   09/28/2019

@Desc    :   This class is a concrete Lion class, it implements the _makeNoise() function.

'''

from Feline import Feline


class Lion(Feline):
	def __init__(self, name):
		super().__init__(name)

	def _makeNoise(self):
		return super()._getName() + " is Aoooooo"