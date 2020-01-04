from MapBase import *


class SortedTableMap(MapBase):
	"""docstring for SortedTableMap"""

	def _find_index(self, k, low, high):
		if high < low:
			return high + 1
		else:
			mid = (low+high)//2
			if k == self.table[mid].key:
				return mid
			elif k < self.table[mid].key:
				return  self._find_index(k, 0, mid-1)
			else :
				return  self._find_index(k, mid+1, high)

	def __init__(self):
		self.table = []


	def __len__(self):
		return len(self.table)


	def __getitem__(self, k):
		j = self._find_index(k, 0, len(self.table)-1)
		if j == len(self.table) or self.table[j].value != k:
			raise KeyError('Key Error: '+ repr(k))
		return self.table[j].value


	def __setitem__(self, k, v):
		j = self._find_index(k, 0, len(self.table)-1)
		if j < len(self.table) and self.table[j].value == k:
			self.table[j].value = v
		else:
			self.table.insert(j, self.Item(k,v))


	def __delitem__(self, k):
		j = self._find_index(k, 0, len(self.table)-1)
		if j == len(self.table) or self.table[j].value != k:
			raise KeyError('Key Error: '+ repr(k))
		self.table.pop(j)


	def __iter__(self):
		for item in self.table:
			yield item.key


	def __reversed__(self):
		for item in reversed(self.table):
			yield item.key


	def find_min(self):
		if len(self.table) > 0:
			return (self.table[0].key, self.table[0].value)
		else:
			return None

	def find_max(self):
		if len(self.table) > 0:
			return (self.table[-1].key, self.table[-1].value)
		else:
			return None


