from Task import Task
from Zoo import Zoo
from ZooAnnouncer import ZooAnnouncer
from Zookeeper import ZooKeeper

zoo = Zoo()
keeper = ZooKeeper(zoo)
announcer = ZooAnnouncer(keeper)

keeper.setTast(Task.ROLL_CALL)
keeper.setTast(Task.FEED)
keeper.setTast(Task.EXERCISE)
keeper.setTast(Task.SHUTDOWN)
