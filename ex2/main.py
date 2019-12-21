from adaptable_heap_priority_queue import *
import time
import re
from job import *
import sys

"""
TO DO : Priority must be increased with aging. Still to do. I miss theory on the matter.

"""
TIME_SLICE = 1
X_TIME_SLICES = int(sys.argv[1] if len(sys.argv) > 1 else exit('Missing argument ... Exiting'))
#prendo il primo argomento a riga di comando e lo uso come X 
Locators = []

#seconds of a time slice
current_executing_job = None


q = AdaptableHeapPriorityQueue()
act_slice = 0
done = False

"""
Usiamo un tempo di arrivo perchè anche se ho due job con stessa priorità e stessa lunghezza, posso dire che quello che sta nella coda da più tempo viene eseguito prima.
(Potrebbe accadere che magari alla slice dopo quella attuale la priorità di quel job sarebbe stata aumentata, ma non lo ha fatto ancora, quindi lui sta da più tempo dentro la coda ed eseguo
prima lui)
"""

def update_queued_jobs(q,Locators):
	global X_TIME_SLICES,act_slice
	if q.is_empty():
		return
	"""
	Quando faccio l'update della priorità ? Quando  - arrival_slice  + actual_slice > X_TIME_SLICES
	"""
	for loc in Locators:
		
		if (act_slice - loc._key[2]) > X_TIME_SLICES:
			key = loc._key
			newkey = (key[0] - 1,)
			newkey = newkey + newkey[1:]
			q.update(loc,newkey,loc._value)


while True:

	update_queued_jobs(q,Locators)
	if current_executing_job:
		print("Slice " + str(act_slice) + " Executing : " + str(current_executing_job))

	else:        
		if not q.is_empty():
			current_executing_job = q.remove_min()[1]
			#remove locator
			done = False
			current_executing_job.executed_slice = act_slice
			print("Slice " + str(act_slice) + ' Executing job ' + str(current_executing_job))
		else:
			print('Slice ' + str(act_slice) + " : No job in execution in this slice")

	command = input("Command: ")    
	#returns a list of values found in a string
	values = re.findall('[0-9]+|-[0-9]+',command)
	if len(values) > 0:
		(length,priority) =  values

		job = Job('Job' + str(act_slice), int(priority), int(length), act_slice)
		"""
		Why am i passing the arrival time as a negative value ? This is because i want to use python comparison between tuples, and a smaller arrival
		time means a longer time passed in the queue. Since the other values need to be compared as greater or greater/equal, this is one way to solve the problem

		Another way would be to override the methods that use comparison in the Heap-based priority queue and use our comparison function. This is a lot more work.
		"""
		key = (job._priority,job._length, job.arrival_slice)
		Locators.append(q.add(key, job))
		

	else:
		pass

	time.sleep(TIME_SLICE)
	act_slice += 1

	if current_executing_job:
		#print(int(current_executing_job._length) + current_executing_job.arrival_slice)
		if (int(current_executing_job._length) + current_executing_job.arrival_slice) < act_slice:
			current_executing_job = None
	print()
	#print(Locators[act_slice - 1]._index)
	#print(Locators.pop()._index)