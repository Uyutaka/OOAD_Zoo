'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Zoo.py

@Time    :   09/28/2019

@Desc    :   This is Zoo which can initialize all animals in it.

'''

from Cat import Cat
from Dog import Dog
from Elephant import Elephant
from Hippo import Hippo
from Lion import Lion
from Rhino import Rhino
from Tiger import Tiger
from Wolf import Wolf
from WolfNoise import WolfNoise
from DogNoise import DogNoise


class Zoo:
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
		animals.append(Elephant("elephant2"))

		animals.append(Cat("cat1"))
		animals.append(Cat("cat2"))

		animals.append(Tiger("tiger1"))
		animals.append(Tiger("tiger2"))

		animals.append(Lion("lion1"))
		animals.append(Lion("lion2"))

		animals.append(Wolf("wolf1", WolfNoise()))
		animals.append(Wolf("wolf2", WolfNoise()))

		animals.append(Dog("dog1", DogNoise()))
		animals.append(Dog("dog2", DogNoise()))

		return animals