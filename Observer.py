from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
	@abstractmethod
	def update(self, task):
		pass
