from Cat import Cat
from Dog import Dog
from Elephant import Elephant
from Hippo import Hippo
from Lion import Lion
from Rhino import Rhino
from Tiger import Tiger
from Wolf import Wolf


class Zoo():
	def __init__(self):
		self.animals = self.__initializeZoo()

	@staticmethod
	def __initializeZoo():
		animals = []

		animals.append(Hippo("hippo1"))
		animals.append(Hippo("hippo2"))

		animals.append(Rhino("rhino1"))
		animals.append(Rhino("rhino2"))

		animals.append(Elephant("elephant1"))
		animals.append(Elephant("elephant1"))

		animals.append(Cat("cat1"))
		animals.append(Cat("cat2"))

		animals.append(Tiger("tiger1"))
		animals.append(Tiger("tiger2"))

		animals.append(Lion("lion1"))
		animals.append(Lion("lion2"))

		animals.append(Wolf("wolf1"))
		animals.append(Wolf("wolf2"))

		animals.append(Dog("dog1"))
		animals.append(Dog("dog2"))

		return animals