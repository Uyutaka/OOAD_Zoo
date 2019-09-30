'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Zookeeper.py

@Time    :   09/28/2019

@Desc    :   This is observable object, which can let ZooAnnouncer know if any updates here.
			Also, It can do different operations in Zoo.
'''

from Subject import Subject
from Task import Task


class ZooKeeper(Subject):
	def __init__(self, zoo):
		self.__zoo = zoo
		self.__task = None
		self.__observers = []

	def registerObserver(self, observer):
		self.__observers.append(observer)

	def removeObserver(self, observer):
		self.__observers.remove(observer)

	def notifyObservers(self):
		for o in self.__observers:
			o.update(self.__task)

	def setTask(self, task):
		self.__task = task
		self.notifyObservers()
		self.__doTask()


	def __doTask(self):

		if self.__task == Task.WAKE:
			self.__wake()
		elif self.__task == Task.ROLL_CALL:
			self.__rollCall()
		elif self.__task == Task.FEED:
			self.__feed()
		elif self.__task == Task.EXERCISE:
			self.__exercise()
		elif self.__task == Task.SHUTDOWN:
			self.__shutdown()

	def __wake(self):
		print("The zookeeper is waking up animals")
		for a in self.__zoo._animals:
			print(a._wakeup())
		print("\n")

	def __rollCall(self):
		print("The zookeeper is rolling call animals")
		for a in self.__zoo._animals:
			print(a._makeNoise())
		print("\n")

	def __feed(self):
		print("The zookeeper is feeding animals")
		for a in self.__zoo._animals:
			print(a._eat())
		print("\n")

	def __exercise(self):
		print("The zookeeper is exercising animals")
		for a in self.__zoo._animals:
			print(a._roam())
		print("\n")

	def __shutdown(self):
		print("The zookeeper is shutting down the zoo")
		for a in self.__zoo._animals:
			print(a._sleep())
		print("\n")