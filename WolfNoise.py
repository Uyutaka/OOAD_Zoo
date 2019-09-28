'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   WolfNoise.py

@Time    :   09/28/2019

@Desc    :   This class implements the MakeNoise interface, as it can help wolf to make noise.

'''

from MakeNoise import MakeNoise

class WolfNoise(MakeNoise):

    def makeNoise(self):
        return " is Aooooooooo(from strategy pattern)"