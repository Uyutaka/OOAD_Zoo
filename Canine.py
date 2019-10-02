'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Canine.py

@Time    :   09/28/2019

@Desc    :   This class is a abstract class inherits from Animal, and it is a base class for all kinds of canine.
            Also, this class work in the strategy pattern. As it uses attribute noiseAlgorithm implementing
            NoiseAlgorithm interface.

'''

from abc import ABCMeta, abstractmethod
from Animal import Animal


class Canine(Animal, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, noiseAlgorithm):
        super().__init__(name)
        self.__noiseAlgorithm = noiseAlgorithm

    def _roam(self):
        return super()._getName() + "is roaming(Canine)."

    def _makeNoise(self):
        return super()._getName() + self.__noiseAlgorithm.makeNoise()