'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Pachyderm.py

@Time    :   09/28/2019

@Desc    :   This class is a abstract class inherits from Animal, and it is a base class for all kinds of Pachyderm.

'''

from abc import ABCMeta
from Animal import Animal


class Pachyderm(Animal, metaclass=ABCMeta):

	def _roam(self):
		return super()._getName() + " is roaming" + " (Pachyderm)"

	def _wakeup(self):
		return super()._getName() +  "is waking up just now (\"Stamp, stamp, Stamp\")"