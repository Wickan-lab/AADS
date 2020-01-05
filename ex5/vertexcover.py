from graph import *
import copy
import time

def remove_edges_vertex(gc,v):
	"""
	Removes all incident edges on the vertex v.
	"""
	remove_edges_v = gc.incident_edges(v)
	covered_vert_v = [e.opposite(v) for e in remove_edges_v]

	for elem in covered_vert_v:
		
		del gc._incoming[elem][v]
		
		if gc._incoming[elem] is None:
			del gc._incoming[elem]
		
	if gc.is_directed():
		remove_edges_v_dir = gc.incident_edges(v,outgoing=False)
		covered_vert_v_dir = [e.opposite(v) for e in remove_edges_v_dir]
		
		for elem in covered_vert_v_dir:
			del gc._outgoing[elem][v]
			
			if gc._outgoing[elem] is None:
				del gc._outgoing[elem]
		
		del gc._incoming[v]
	del gc._outgoing[v]

	return gc

def vc_approx_2(gc):
	"""
	Calculates the who needs to have the software in the BaceFook network graph.
	Reminder : g is the BaceFook netowrk graph representation
	"""
	c = []
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
