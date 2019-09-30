'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   DogNoiseAlgorithm.py

@Time    :   09/28/2019

@Desc    :   This class implements the NoiseAlgorithm interface, as it can help dog to make noise.

'''

from NoiseAlgorithm import NoiseAlgorithm

class DogNoise(NoiseAlgorithm):

    def makeNoise(self):
        return " is Wang Wang(from strategy parttern)"