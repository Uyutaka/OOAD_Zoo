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
