'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   ZooAnnouncer.py

@Time    :   09/28/2019

@Desc    :   This is observer, which observes the Zookeeper to see if any updates.

'''

from Observer import Observer


class ZooAnnouncer(Observer):
	def __init__(self, zooKeeper):
		self.__zooKeeper = zooKeeper
		self.__zooKeeper.registerObserver(self)
		self.__task = None

	def update(self, task):
		self.__task = task
		self.__announce()

	def __announce(self):
		print(f"Hi, this is the ZooAnnouncer. The Zookeeper is about to {self.__task.value} the animals!")
