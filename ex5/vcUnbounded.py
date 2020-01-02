from graph import *
import copy
import time

def vc(g):
	c = []
	gc = copy.deepcopy(g)
	
	vert = gc.vertices()
	edges = gc.edges()

	while gc.edges():
		#should be done everytime to adjust degree after removing
		v_sort = sorted(gc.vertices(), key= lambda e : gc.degree(e), reverse=True)
		v = v_sort[0]
		c.append(v)		

		gc = remove_edges_vertex(gc,v)

	return c