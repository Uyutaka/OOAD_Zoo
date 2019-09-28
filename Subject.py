'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Subject.py

@Time    :   09/28/2019

@Desc    :   This is interface as Subject.

'''

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
	@abstractmethod
	def registerObserver(self, observer):
		pass

	@abstractmethod
	def removeObserver(self, observer):
		pass

	@abstractmethod
	def notifyObservers(self):
		pass
