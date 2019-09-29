'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   DogNoise.py

@Time    :   09/28/2019

@Desc    :   This class implements the MakeNoise interface, as it can help dog to make noise.

'''

from MakeNoise import MakeNoise

class DogNoise(MakeNoise):

    def makeNoise(self):
        return " is Wang Wang(from strategy parttern)"