from adaptable_heap_priority_queue import *
import time
import re
from job import *

TIME_SLICE = 1
#seconds of a time slice
current_executing_job = None

class MyAdaptablePriorityQueue(AdaptableHeapPriorityQueue):
	"""
	override dei metodi ustai per costruire heap e fare confronti
	"""



q = AdaptableHeapPriorityQueue()
act_slice = 0
"""
Usiamo un tempo di arrivo perchè anche se ho due job con stessa priorità e stessa lunghezza, posso dire che quello che sta nella coda da più tempo viene eseguito prima.
(Potrebbe accadere che magari alla slice dopo quella attuale la priorità di quel job sarebbe stata aumentata, ma non lo ha fatto ancora, quindi lui sta da più tempo dentro la coda ed eseguo
prima lui)
"""

while True:

	if current_executing_job:
		print("Slice " + str(i) + " Executing : " + str(current_executing_job))

	else:        
		if not q.is_empty():
			current_executing_job = q.min()[-1]
			current_executing_job.executed_slice = act_slice
			print('Executing job ' + str(current_executing_job))
		else:
			print("No job in execution in this slice")

	
	command = input("Command: ")    
	#returns a list of values found in a string
	values = re.findall('[0-9]+|-[0-9]+',command)
	if len(values) > 0:
		(length,priority) =  values
		job = Job('Job' + str(act_slice), priority, length, act_slice)        
		q.add(job._priority,job)

	else:
		pass

	time.sleep(TIME_SLICE)
	act_slice += 1

	if current_executing_job:
		if int(current_executing_job._length) + current_executing_job.arrival_slice < act_slice:
			current_executing_job = None
			
