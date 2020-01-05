from adaptable_heap_priority_queue import *
import time
import re
from job import *
import sys
import math

act_slice = 0
alfa = float(sys.argv[1] if len(sys.argv) > 1 else 1/2)
if not(0 <= alfa <= 1):
	print('Invalid alfa value, using default value')
	alfa = 1/2

print("alfa value " + str(alfa))

class ex2_apq(AdaptableHeapPriorityQueue):

	def view(self):
		"""
		Returns a set-like view of the queue to iterate on
		"""
		return self._data

def update_queued_jobs(q,X):
	"""
	searches the entire Locators data structure and updates jobs if needed. That is when 
	a job has been waiting for more than X time slices, or another slice has passed,
	therefore incrementing its waiting time in the queue. 
	"""
	if q.is_empty():
		return
	for loc in q.view():
		#print(loc._key)
		priority = loc._key	
		oldjob = loc._value

		if (oldjob.waiting_time) >= X:
			if -20 < priority <= 19:
				print('increasing priority of ' + str(oldjob._name))
				#resetting waiting time
				newvalue = Job(oldjob._name,oldjob._priority - 1,oldjob._length, oldjob.arrival_slice, 0,oldjob.executed_slice)

		else:
			print('increasing waiting_time ' + str(oldjob._name))
			newvalue = Job(oldjob._name,oldjob._priority,oldjob._length, oldjob.arrival_slice, oldjob.waiting_time + 1,oldjob.executed_slice)

		#update edits
		newkey = newvalue._priority
		q.update(loc,newkey,newvalue)
			
def update_X(t,tau,alfa=1/2):	
	#print("Float tau " + str(alfa * t + (1 - alfa) * tau))
	return math.ceil(alfa * t + (1 - alfa) * tau)

def main():
	global act_slice,alfa
	current_executing_job = None
	q = ex2_apq()
	tau = 1

	while True:

		update_queued_jobs(q,tau)

		if current_executing_job:
			print("Slice " + str(act_slice) + " Executing : " + str(current_executing_job))
		else:        
			if not q.is_empty():
				current_executing_job = q.remove_min()[1]
				current_executing_job.executed_slice = act_slice				
				print("Slice " + str(act_slice) + ' Executing job ' + str(current_executing_job))

				tau = update_X(current_executing_job._length,tau,alfa=alfa)
			else:
				print('Slice ' + str(act_slice) + " : No job in execution in this slice")

		command = input("Command: ")    
		split_command = command.split(' ')
			
		if len(split_command) == 8:

			(name,length,priority) = (split_command[1],split_command[4],split_command[7])

			if 0 < int(length) <= 100 and -20 <= int(priority) <= 19:
				job = Job(name, int(priority), int(length), act_slice)
				key = job._priority
				q.add(key,job)
			else:
				print('Invalid values, skipping to the next slice')
		else:
			print('No job inserted in this slice/invalid command')

		act_slice += 1

		if current_executing_job:
			if (int(current_executing_job._length) + current_executing_job.executed_slice) <= act_slice:
				current_executing_job = None
		print()

if __name__ == '__main__':
	main()
