from Feline import Feline
import random


class Cat(Feline):
	def __init__(self, name):
		super().__init__(name)

	def _makeNoise(self):
		r = random.randint(0,2)
		switcher = {
			0: self.__meow,
			1: self.__layDown,
			2: self.__sharpenClaws
		}
		func = switcher.get(r)
		return func()

	def __meow(self):
		return super()._getName() + " is meowing."

	def __layDown(self):
		return super()._getName() + " is laying down."

	def __sharpenClaws(self):
		return super()._getName() + " is sharpening claws."
