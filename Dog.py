'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Dog.py

@Time    :   09/28/2019

@Desc    :   This class is a concrete Dog class, it participates in the strategy pattern.

'''

from Canine import Canine


class Dog(Canine):
	def __init__(self, name, noiseAlgorithm):
		super().__init__(name, noiseAlgorithm)
