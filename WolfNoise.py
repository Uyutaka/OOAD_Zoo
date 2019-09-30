'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   WolfNoiseAlgorithm.py

@Time    :   09/28/2019

@Desc    :   This class implements the NoiseAlgorithm interface, as it can help wolf to make noise.

'''

from NoiseAlgorithm import NoiseAlgorithm

class WolfNoise(NoiseAlgorithm):

    def makeNoise(self):
        return " is Aooooooooo(from strategy pattern)"