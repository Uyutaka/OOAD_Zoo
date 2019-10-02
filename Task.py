'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   Task.py

@Time    :   09/28/2019

@Desc    :   This is a helper class enumerate all kinds of tasks.

'''

from enum import Enum


class Task(Enum):
	WAKE = "wake"
	ROLL_CALL = "roll call"
	FEED = "feed"
	EXERCISE = "exercise"
	SHUTDOWN = "shutdown"
