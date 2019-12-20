class Job:
	__slots__ = '_priority', '_length', '_name', 'arrival_slice','executed_slice'
	"""
	Secondo me raga potrebbe volerci anche un tempo di arrivo e un tempo di esecuzione per motivi che spiego nel main
	"""

	def __init__(self, name, priority, length,arrival_slice,executed_slice=-1):
		assert(arrival_slice >= 0)
		self._name = name
		self._priority = priority
		self._length = length
		self.arrival_slice = arrival_slice
		self.executed_slice = executed_slice

	def __str__(self):
		return "[" + str(self._name) + "]" + 'Length : ' + str(self._length) + " Priority : " + str(self._priority) + ' Arrived at : ' + str(self.arrival_slice)
	def getpriority(self):
		return self._priority

	def setpriority(self, value):
		self._priority = value

	def delpriority(self):
		del self._priority

	


	def getlength(self):
		return self._length

	def setlength(self, value):
		self._length = value

	def dellength(self):
		del self._length


	def getname(self):
		return self._name

	def setname(self,value):
		self._name = value

	def delname(self):
		del self._name




	priority_property = property(getpriority, setpriority, delpriority, "I'm the 'priority' property.")
	length_property = property(getlength, setlength, dellength , "I'm the 'length' property.")
	name_property = property(getname, setname, delname , "I'm the 'name' property.")

	"""
	La property è il modo pythonico di fare i getter e i setter, in questo modo anche quando all'utente sembra di accedere all'attributo di una classe facendo
	j.name allora viene chiamato il getter a sua insaputa
	j.name = name
	setter viene chiamato
	del j.name il deleter viene chiamato
	"""


	def greater(self,b):
		return self._priority > b.priority

	def greater_equal(self,b):
		pass

	def less(self,b):
		return not greater_equal()

	def less_equal(self,b):
		return not greater()

