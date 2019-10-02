# Zoo
### Project2 for CSCI5448 (OOAD)

Team Member: 
* Yutaka Urakami
* Mengyu Wu
* Hao Wu 

### Instruction for running the code:
Our code is base on Python 3.7. To run the code, execute main.py. And the output in the console is in the [ouput.txt](/output.txt).

Especially, for two design patterns:
* Observer Pattern: The Zookeeper object is the subject, the ZooAnnouncer object is observer. The state in the subject(ZooKeeper) is different operations/tasks to exercise animals.
* Strategy pattern: We use strategy pattern in Canine and its two subclasses which are Dog and Wolf. We define a interface called NoiseAlgorithm, and the Canine object have a attribute to use this interface to perform different ways to make noise. The interface will be initialized in Canine's constructor.