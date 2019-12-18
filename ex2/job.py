class Job:
    __slots__ = '_priority', '_length', '_name'

    def __init__(self, name, priority, length):
       self._name = name
       self._priority = priority
       self._length = length

    def __str__(self):
        return "[" + str(self._name) + "]" + str(self._lenght) + " " + str(self._priority)



