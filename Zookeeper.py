class ZooKeeper():
	def _wake(self, animals):
		print("The zookeeper is waking up animals")
		for a in animals:
			print(a._wakeup())
		print("\n")

	def _rollCall(self, animals):
		print("The zookeeper is rolling call animals")
		for a in animals:
			print(a._makeNoise())
		print("\n")

	def _feed(self, animals):
		print("The zookeeper is feeding animals")
		for a in animals:
			print(a._eat())
		print("\n")

	def _exercise(self, animals):
		print("The zookeeper is exercising animals")
		for a in animals:
			print(a._roam())
		print("\n")

	def _shutdown(self, animals):
		print("The zookeeper is shutting down the zoo")
		for a in animals:
			print(a._sleep())
		print("\n")