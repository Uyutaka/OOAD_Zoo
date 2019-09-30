from abc import ABCMeta, abstractmethod
from Animal import Animal


class Canine(Animal, metaclass=ABCMeta):

    def __init__(self, name, noiseAlgorithm):
        super().__init__(name)
        self.__noiseAlgorithm = noiseAlgorithm

    def _roam(self):
        return super()._getName() + "is roaming(Canine)."

    def _makeNoise(self):
        return super()._getName() + self.__noiseAlgorithm.makeNoise()