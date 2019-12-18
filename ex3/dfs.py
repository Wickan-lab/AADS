# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import time
def DFS(g, u, discovered):
	"""Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

	discovered is a dictionary mapping each vertex to the edge that was used to
	discover it during the DFS. (u should be "discovered" prior to the call.)
	Newly discovered vertices will be added to the dictionary as a result.
	"""
	for e in g.incident_edges(u):    # for every outgoing edge from u
		v = e.opposite(u)
		if v not in discovered:        # v is an unvisited vertex
			discovered[v] = e            # e is the tree edge that discovered v
			DFS(g, v, discovered)        # recursively explore from v

def construct_path(u, v, discovered):
	"""
	Return a list of vertices comprising the directed path from u to v,
	or an empty list if v is not reachable from u.

	discovered is a dictionary resulting from a previous call to DFS started at u.
	"""
	path = []                        # empty path by default
	if v in discovered:
		# we build list from v to u and then reverse it at the end
		path.append(v)
		walk = v
		while walk is not u:
			e = discovered[walk]         # find edge leading to walk
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		path.reverse()                 # reorient path from u to v
	return path

def DFS_complete(g):
	"""Perform DFS for entire graph and return forest as a dictionary.

	Result maps each vertex v to the edge that was used to discover it.
	(Vertices that are roots of a DFS tree are mapped to None.)
	"""
	forest = {}
	for u in g.vertices():
		if u not in forest:
			forest[u] = None             # u will be the root of a tree
			DFS(g, u, forest)
	return forest

"""Exercise 3 iterative DFS"""

def iterative_dfs(g, u,DEBUG=False):
	"""A version of the DFS algorithm, good ol' iterative."""

	if g.degree(u) == 0:
		print("Only root Graph")
		return
	
	new = None
	act = u
	prec = None

	going_back = False

	new_edge = None
	act_edge = None
	prev_edge = None
	#prendi gli archi incidenti al vertice attuale
	#considera tutti gli archi incidenti, se sono unexplored, visita il vertice, altrimenti passa al prossimo arco se non è discovery
	#se non ci sono altri archi termina, altrimenti ripeti dal punto 1	
	i = 0

	#tolgo la u

	print(g.vertex_count())

	while i < (g.vertex_count()):

		if not act.is_visited():
			act.set_visited()
			i+=1
			if DEBUG:
				print('Incrementing i ' + str(i))
				print()

		#print(i)
		#print([str(x) for x in g.incident_edges(act)])

		if not going_back:
			print("DFS " + str(act) + ' ' + str(act_edge))
		else:
			if DEBUG:
				print("DEBUG (back) DFS " + str(act) + ' ' + str(act_edge))
			going_back = False

		edges = g.incident_edges(act)

		for e in edges:
			if DEBUG:
				print("Possible new Node " + str(e.opposite(act)))

			if e.is_unexplored():

				if not e.opposite(act).is_visited():
					##evita blind spot
					if g.degree(e.opposite(act)) <= 1:

						blind_spot = e.opposite(act)
						blind_spot.set_visited()
						e.set_discovery()
						print("blind_spot DFS " + str(blind_spot) + ' ' + str(e))
						i += 1
						if DEBUG:
							print('Incrementing i for a blind spot ' + str(i))
							print()
						
						#se il while si conclude con questa i allora la condizione non + verificata subito e avviene una stampa un più ?
						#non andrò in quei nodi quindi incremento

					else:

						new = e.opposite(act)
						if DEBUG:
							print("New node " + str(new))
						e.set_discovery()
						new_edge = e
						
						break
						"""Che succede se un nodo ha solo blind spot ? Chi è il new ?"""

				else:
					#setta un back_edge
					if DEBUG:
						print("Edge " + str(e) + " is now set as back")
					e.set_back()
		"""
		"""
		if DEBUG:
			print("Act " + str(act) + " is now set as visited")
		"""
		"""
		if new == act:
			#nodo con solo blind spot			
			b_edges = g.incident_edges(act)
			for e in b_edges:
				if not e.is_unexplored() and not e.is_forbidden():
					if DEBUG:
						print('Going in a back edge ' + str(e))
					if prec != e.opposite(act):
						prec = e.opposite(act)
						e.set_forbidden()
						break
					#questo evita di tornare sempre al nodo in cui mi trovavo prima
					#di percorrere il primo back edge
				
			new = prec
			going_back = True

			if DEBUG:
				print("Nodo " + str(act) + " solo con blind spot. Setto come new node " + str(prec))
		else:			
			#i+=1
			pass


		prec = act
		act = new
		act_edge = new_edge	
		if DEBUG:
			time.sleep(1)

	print('Final i : ' + str(i))