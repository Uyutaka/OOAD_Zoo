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
		self.zoo = zoo
		self.task = None
		self.observers = []

	def registerObserver(self, observer):
		self.observers.append(observer)

	def removeObserver(self, observer):
		self.observers.remove(observer)

	def notifyObservers(self):
		for o in self.observers:
			o.update(self.task)

	def setTask(self, task):
		self.task = task
		self.notifyObservers()
		self.doTask()

	def getTask(self, task):
		return task

	def doTask(self):

		if self.task == Task.WAKE:
			self._wake()
		elif self.task == Task.ROLL_CALL:
			self._rollCall()
		elif self.task == Task.FEED:
			self._feed()
		elif self.task == Task.EXERCISE:
			self._exercise()
		elif self.task == Task.SHUTDOWN:
			self._shutdown()

	def _wake(self):
		print("The zookeeper is waking up animals")
		for a in self.zoo.animals:
			print(a._wakeup())
		print("\n")

	def _rollCall(self):
		print("The zookeeper is rolling call animals")
		for a in self.zoo.animals:
			print(a._makeNoise())
		print("\n")

	def _feed(self):
		print("The zookeeper is feeding animals")
		for a in self.zoo.animals:
			print(a._eat())
		print("\n")

	def _exercise(self):
		print("The zookeeper is exercising animals")
		for a in self.zoo.animals:
			print(a._roam())
		print("\n")

	def _shutdown(self):
		print("The zookeeper is shutting down the zoo")
		for a in self.zoo.animals:
			print(a._sleep())
		print("\n")