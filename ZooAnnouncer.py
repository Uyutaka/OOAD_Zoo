'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   ZooAnnouncer.py

@Time    :   09/28/2019

@Desc    :   This is observer, which observes the Zookeeper to see if any updates.

'''

from Observer import Observer


class ZooAnnouncer(Observer):
	def __init__(self, zooKeeper):
		self.zooKeeper = zooKeeper
		self.zooKeeper.registerObserver(self)
		self.task = None

	def update(self, task):
		self.task = task
		self.announce()

	def announce(self):
		print(f"Hi, this is the ZooAnnouncer. The Zookeeper is about to {self.task.value} the animals!")
