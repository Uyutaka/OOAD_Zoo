'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   NoiseAlgorithm.py

@Time    :   09/28/2019

@Desc    :   This is interface for NoiseAlgorithm, as it is used for strategy pattern.

'''

from abc import ABCMeta, abstractmethod

class NoiseAlgorithm(metaclass=ABCMeta):
    @abstractmethod
    def makeNoise(self):
        pass
