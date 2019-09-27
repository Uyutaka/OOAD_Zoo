from enum import Enum


class Task(Enum):
	WAKE = "wake"
	ROLL_CALL = "roll call"
	FEED = "feed"
	EXERCISE = "exercise"
	SHUTDOWN = "shutdown"
