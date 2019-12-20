from adaptable_heap_priority_queue import *
import time
import re
from job import *
import sys

"""
TO DO : Priority must be increased with aging. Still to do. I miss theory on the matter.
"""
TIME_SLICE = 1
X_TIME_SLICES = 5 #giusto una prova
#X_TIME_SLICES = sys.argv[1] if len(sys.argv) > 1 else exit('Missing argument ... Exiting')
#questo lo ha scritto Peppe ma non mi piace :P
# prendo il primo argomento a riga di comando e lo uso come X


# seconds of a time slice
current_executing_job = None


class MyAdaptablePriorityQueue(AdaptableHeapPriorityQueue):
    """
    override dei metodi ustai per costruire heap e fare confronti
    """


q = AdaptableHeapPriorityQueue()
act_slice = 0
done = False
"""
Usiamo un tempo di arrivo perchè anche se ho due job con stessa priorità e stessa lunghezza, posso dire che quello che sta nella coda da più tempo viene eseguito prima.
(Potrebbe accadere che magari alla slice dopo quella attuale la priorità di quel job sarebbe stata aumentata, ma non lo ha fatto ancora, quindi lui sta da più tempo dentro la coda ed eseguo
prima lui)
"""

while True:

    if current_executing_job:
        print("Slice " + str(act_slice) + " Executing : " + str(current_executing_job))

    else:
        if not q.is_empty():
            current_executing_job = q.remove_min()[1]
            done = False
            current_executing_job.executed_slice = act_slice
            print("Slice " + str(act_slice) + ' Executing job ' + str(current_executing_job))
        else:
            print('Slice ' + str(act_slice) + " : No job in execution in this slice")

    command = input("Command: ")
    # returns a list of values found in a string
    values = re.findall('[0-9]+|-[0-9]+', command)



    if len(values) > 0:
        if 1 <= int(values.__getitem__(0)) <= 100 and -20 <= int(values.__getitem__(1)) <= 19:
            (length, priority) = values
            job = Job(int(priority), int(length), act_slice)
            q.add(job._priority, job)
        else:
            print("Insert a length between 1 and 100 and a priority between -20 and 19.")
            continue
    else:
        pass

    time.sleep(TIME_SLICE)
    act_slice += 1

    if current_executing_job:
        # print(int(current_executing_job._length) + current_executing_job.arrival_slice)
        if (int(current_executing_job._length) + current_executing_job.arrival_slice) < act_slice:
            current_executing_job = None
    print()
