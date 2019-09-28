'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   MakeNoise.py

@Time    :   09/28/2019

@Desc    :   This is interface for MakeNoise, as it is used for strategy pattern.

'''

from abc import ABCMeta, abstractmethod

class MakeNoise(metaclass=ABCMeta):
    @abstractmethod
    def makeNoise(self):
        pass
