from adaptable_heap_priority_queue import *
import time
TIME_SLICE = 1
#seconds of a time slice
current_executing_job = None

class MyAdaptablePriorityQueue(AdaptableHeapPriorityQueue):
    """
    override dei metodi ustai per costruire heap e fare confronti
    """



q = AdaptableHeapPriorityQueue()
i = 0
"""
Usiamo un tempo di arrivo perchè anche se ho due job con stessa priorità e stessa lunghezza, posso dire che quello che sta nella coda da più tempo viene eseguito prima.
(Potrebbe accadere che magari alla slice dopo quella attuale la priorità di quel job sarebbe stata aumentata, ma non lo ha fatto ancora, quindi lui sta da più tempo dentro la coda ed eseguo
prima lui)
"""
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
