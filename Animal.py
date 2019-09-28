'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Animal.py

@Time    :   09/28/2019

@Desc    :   This class is a abstract class, and it is a base class for all kinds of animals.

'''

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name):
        self.__name = name

    def _getName(self):
        return self.__name + " (" + self.__class__.__name__ + ")"

    def _sleep(self):
        return self._getName() + " is sleeping (Zzzzz)"

    def _wakeup(self):
        return self._getName() + " waked up just now"

    def _eat(self):
        return self._getName() + " is eating"

    @abstractmethod
    def _makeNoise(self):
        pass

    @abstractmethod
    def _roam(self):
        pass