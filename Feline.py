'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Feline.py

@Time    :   09/28/2019

@Desc    :   This class is a abstract class inherits from Animal, and it is a base class for all kinds of feline.

'''

from abc import ABCMeta, abstractmethod
from Animal import Animal


class Feline(Animal, metaclass=ABCMeta):
	@abstractmethod
	def __init__(self, name):
		super().__init__(name)

	def _roam(self):
		return super()._getName() +  "is roaming (Feline)"