'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Wolf.py

@Time    :   09/28/2019

@Desc    :   This class is a concrete Wolf class, it participates in the strategy pattern.

'''

from Canine import Canine


class Wolf(Canine):
	def __init__(self, name, noiseAlgorithm):
		super().__init__(name, noiseAlgorithm)
