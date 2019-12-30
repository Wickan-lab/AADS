from graph import *
import copy
import time

def vc(g):
	c = []
	gc = copy.deepcopy(g)
	
	vert = gc.vertices()
	edges = gc.edges()
	#v_sort = sorted(gc.vertices(), key= lambda e : gc.degree(e), reverse=True)	

	while gc.edges():
		#should be done everytime to adjust degree after removing
		v_sort = sorted(gc.vertices(), key= lambda e : gc.degree(e), reverse=True)
		#print([str(x) for x in gc.edges()])
		v = v_sort[0]

		#print("Vertex : " + str(v))
		c.append(v)		

		gc = remove_edges_vertex(gc,v)

	return c

def remove_edges_vertex(gc,v):
	"""
	Removes all incident edges on the vertex v, then removes vertex v.
	"""
	remove_edges_v = gc.incident_edges(v)
	covered_vert_v = [e.opposite(v) for e in remove_edges_v]

	for elem in covered_vert_v:
		del gc._outgoing[elem][v]
		if gc._outgoing[elem] is None:
			del gc._outgoing[elem]
	del gc._outgoing[v]

	return gc


		
#non cancellare il vertice ma cancella l'edge
"""
remove_edges = gc.incident_edges(v)	
covered_vert = [e.opposite(v) for e in remove_edges]
for elem in covered_vert:
	del gc._outgoing[elem][v]
	if gc._outgoing[elem] is None:
		del gc._outgoing[elem]

del gc._outgoing[v]
"""

def vc_approx_2(g):
	c = []
	gc = copy.deepcopy(g)
	#v_sort = sorted(gc.vertices(), key= lambda e : gc.degree(e), reverse=True)	
	i = 0
	while gc.edges():

		#print([str(x) for x in gc.edges()])

		e = list(gc.edges())[0]		

		u,v = e.endpoints()
		#print('endpoints ' + str(i) + ' : ' + str(u) + ' ' + str(v))
		i+=1
		c.append(u)
		c.append(v)

		gc = remove_edges_vertex(gc, v)
		gc = remove_edges_vertex(gc, u)

	return c
