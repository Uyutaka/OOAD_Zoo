from abc import ABCMeta, abstractmethod
from Animal import Animal

class Canine(Animal, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, makeNoise=None):
        super().__init__(name)


    def _roam(self):
        return super()._getName() + " is roaming (Canine)"