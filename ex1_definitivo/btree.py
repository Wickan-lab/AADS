from tree import *
from sortedtablemap import *




class BTree():
	#__slots__ = "root", "b"
	def __init__(self, b):
		self.root = self.BTreeNode(None)
		self.b = b
		self.len = 0

	class BTreeNode(SortedTableMap):

		# 1) root property: la radice ha almeno ceil((b-1)/2) e al max b figli.
		# 2) node size property: ogni nodo interno (che non sia la radice) ha almeno a figli e al max b figli.
		# 3) depth property: tutte le foglie hanno la stessa profondità
		def __init__(self,p):
			super().__init__()
			self.parent = p
			self.toppa = SortedTableMap()

		def _find_index(self, k, low, high):
			if high < low:
				return low
			else:
				mid = (low+high)//2

				if k == self.table[mid].key:
					return mid
				elif k < self.table[mid].key:
					return  self._find_index(k, 0, mid-1)
				else :
					return  self._find_index(k, mid+1, high)

		def __getitem__(self, k):
			j = self._find_index(k, 0, len(self.table)-1)
			if j == len(self.table):
				return (False,self.toppa)
			if self.table[j].key != k:
				#raise KeyError('Key Error: '+ repr(k))
				return (False,self.table[j].value)

			return (True, self.table[j].value)

	# ---------- private behaviours ----------


	# ---------- public behaviours -----------

	def get_root(self):
		return self.root

	def parent(self, node):
		return node.parent

	def num_children(self, node):
		print(node)
		if node.toppa != None:
			none = 0
		else:
			none = 1
		"""
		none = 0
		
		first = node.find_min()

		print(first)
		if first[1][0] == None:
			none += 1
		if first[1][1] == None:
			none += 1
		"""
		for key in node:
			"""
			if first[0] == key:
				continue
			"""
			#print(node[key])
			if node[key][1] is None:
				none += 1
		

		return len(node) + 1 - none


	def children(self, node):
		#decidere se restituire i None oppure no
		"""
		r = []
		for c in node.values():
			if c[1] != None:
				r.append(c[1])
		if node.toppa == None or len(node.toppa) == 0:
			return r
		else:
			return r.append(node.toppa)
		"""
		if node.toppa is not None:
			return [node[x] for x in node] + [node.toppa[x] for x in node.toppa]  
		return node.values()

	def __len__(self):
		return self.len


	def search(self, root , k):
		"""
		Returns None if the node containing k is not found, otherwise returns the key-containing node
		"""
		if len(root) == 0:
			return None
		if root == None:
			return None

		fi = root[k]
		print(fi[1])
		#found , index
		if not fi[0]:
			return self.search(fi[1],k)
		else:
			return root

	def check_root_property(self):
		# 1) root property: la radice ha almeno a e al max b figli.
		import math
		if self.num_children(self.root) in range(math.ceil((self.b + 1)/2), self.b + 1):
			return True
		return False

	def is_leaf(self, node):
		return self.num_children(node) == 0

	def _height2(self, root):                  # time is linear in size of subtree
	
		if self.is_leaf(root):
		  return 0
		else:
		  return 1 + max(self._height2(c) for c in self.children(root))

	def height(self, node=None):
		if node is None:
			node = self.get_root()
			print(str(node))
		return self._height2(node)        # start _height2 recursion

	def LevelOrder(self): 
		h = height(self.get_root())
		print(h)
		#avoid last level, not needed, and avoid root
		for i in range(2, h): 
			givenLevel(root, i)  

	def givenLevel(self,root , level): 
		level_nodes = []

		if root is None: 
			return
		if level == 1: 
			return level_nodes.append(root)
		elif level > 1 : 
			for c in self.children():
				level_nodes.append(givenLevel(c,level - 1))

	def check_node_size_property(self, a, b ):
		if self.firstMap.__len__() < 1:
			pass
		if self.secondMap.__len__() in range(a, b):
			return True
		else:
			return False

	def check_depth_property(self):
		for k in self.firstMap.keys():
			if self.is_leaf():
				d = self.depth(k)
				break
		for k in self.firstMap.keys():
			if self.is_leaf():
				if self.depth(k).__ne__(d):
					return False
		return True



	def insert(self, k, values):
		"""insert a new node (new key in the map) """
		self.firstMap.__setitem__(k, values)
		#if (not(self.is_empty() and (self.check_depth_property() or self.check_root_property() or self.check_depth_property()))):


	#RIBILANCIA




	def delete(self, k, values):
		self.firstMap.__delitem__(k, values)
	   # if (not(self.check_depth_property() or self.check_root_property() or self.check_depth_property())):
	#RIBILANCIA


	# def rebalance()









