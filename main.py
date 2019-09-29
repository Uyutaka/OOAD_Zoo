from Task import Task
from Zoo import Zoo
from ZooAnnouncer import ZooAnnouncer
from Zookeeper import ZooKeeper

zoo = Zoo()
keeper = ZooKeeper(zoo)
announcer = ZooAnnouncer(keeper)

keeper.setTask(Task.ROLL_CALL)
keeper.setTask(Task.FEED)
keeper.setTask(Task.EXERCISE)
keeper.setTask(Task.SHUTDOWN)
