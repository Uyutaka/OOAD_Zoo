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
