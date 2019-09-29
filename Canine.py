from abc import ABCMeta, abstractmethod
from Animal import Animal


class Canine(Animal, metaclass=ABCMeta):

    def __init__(self, name, makeNoise):
        super().__init__(name)
        self.makeNoise = makeNoise

    def _roam(self):
        return super()._getName() + "is roaming(Canine)."

    def _makeNoise(self):
        return super()._getName() + self.makeNoise.makeNoise()