'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Observer.py

@Time    :   09/28/2019

@Desc    :   This is interface as Observer. Which has update function and
			observer can update it's state by get notification from observable.

'''

from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
	@abstractmethod
	def update(self, task):
		pass
