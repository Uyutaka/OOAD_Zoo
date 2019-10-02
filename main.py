'''
@Author  :   Yutaka Urakami, Hao Wu, Linus Wu

@File    :   main.py

@Time    :   09/28/2019

@Desc    :   This class is a main() function of this project. It can output some basic information on the console.

'''

from Task import Task
from Zoo import Zoo
from ZooAnnouncer import ZooAnnouncer
from Zookeeper import ZooKeeper

zoo = Zoo()
keeper = ZooKeeper(zoo)
announcer = ZooAnnouncer(keeper)

keeper.setTask(Task.WAKE)
keeper.setTask(Task.ROLL_CALL)
keeper.setTask(Task.FEED)
keeper.setTask(Task.EXERCISE)
keeper.setTask(Task.SHUTDOWN)

keeper.removeObserver(announcer)
