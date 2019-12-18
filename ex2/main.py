from adaptable_heap_priority_queue import *
import time
TIME_SLICE = 1
#seconds of a time slice
current_executing_job = None

class MyAdaptablePriorityQueue(AdaptableHeapPriorityQueue):
    pass


q = AdaptableHeapPriorityQueue()
i = 0
while True:
    if current_executing_job:
        print("Slice " + str(i) + " Executing : " + str(current_executing_job))
    else:
        print("No job in execution yet")

    command = input("Command: ")
    if command == 'add command':

        if q.is_empty():
            current_executing_job = 'new job with parameter from previous command'
        else:
            q.add('new job')

    elif command == 'no new job command':
        pass

    time.sleep(TIME_SLICE)
