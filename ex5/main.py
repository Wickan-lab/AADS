from graph import *
from dfs import *
from vertexcover import *
import random
import time

def main():
	#g = Graph()

	start_time = time.time()
	
	n_vert = 100

	
	rows = n_vert
	cols = rows
	#matrix = [[random.getrandbits(1) for x in range(cols)] for x in range(rows)]
	matrices = [[[random.getrandbits(1) for x in range(cols)] for x in range(rows)] for x in range(100)]
	graphs = []
	i = 0
	for matr in matrices:
		g = Graph()
		#inserisci i vertici
		for i in range(n_vert):
			g.insert_vertex(str(i))
		vert = list(g.vertices())
		#completa il grafo
		for n in range(rows):
			for m in range(cols):
				if matr[n][m] == 1 and n != m and not g.get_edge(vert[n],vert[m]):
					g.insert_edge(vert[n],vert[m])

		graphs.append(g)
	
	print("--- %s seconds to create 100 graphs of 100 vertices---" % (time.time() - start_time))

	start_time = time.time()

	for g in graphs:
		vc_approx_2(g)

	print("--- %s seconds to execute the algorithm (bounded)---" % (time.time() - start_time))

	start_time = time.time()
	for g in graphs:
		vc(g)

	print("--- %s seconds to execute the algorithm (UNbounded)---" % (time.time() - start_time))


	"""
	u = g.insert_vertex('u')
	t = g.insert_vertex('t')
	v = g.insert_vertex('v')
	z = g.insert_vertex('z')
	f = g.insert_vertex('f')
	w = g.insert_vertex('w')
	h = g.insert_vertex('h')
	a = g.insert_vertex('a')
	b = g.insert_vertex('b')
	c = g.insert_vertex('c')

	u_t = g.insert_edge(u,t)
	t_w = g.insert_edge(t,w)
	t_f = g.insert_edge(t,f)
	f_v = g.insert_edge(f,v)
	v_z = g.insert_edge(v,z)
	z_u = g.insert_edge(z,u)
	w_a = g.insert_edge(w,a)
	w_b = g.insert_edge(w,b)
	z_h = g.insert_edge(z,h)

	h_c = g.insert_edge(h,c)
	w_f = g.insert_edge(w,f)
	"""
	"""
	n1 = g.insert_vertex('1')
	n3 = g.insert_vertex('3')
	n2 = g.insert_vertex('2')
	n5 = g.insert_vertex('5')
	n7 = g.insert_vertex('7')
	n4 = g.insert_vertex('4')
	n6 = g.insert_vertex('6')

	e14 = g.insert_edge(n1,n4)
	e25 = g.insert_edge(n2,n5)
	e12 = g.insert_edge(n1,n2)
	e56 = g.insert_edge(n5,n6)
	e23 = g.insert_edge(n2,n3)
	e36 = g.insert_edge(n3,n6)
	e37 = g.insert_edge(n3,n7)
	"""

	"""
	n1 = g.insert_vertex('1')
	n3 = g.insert_vertex('3')
	n2 = g.insert_vertex('2')
	n4 = g.insert_vertex('4')

	n12 = g.insert_edge(n1,n2)
	n13 = g.insert_edge(n1,n3)
	n23 = g.insert_edge(n2,n3)
	n14 = g.insert_edge(n1,n4)
	n24 = g.insert_edge(n2,n4)
	n34 = g.insert_edge(n3,n4)
	"""

	#print([str(x) for x in vc(g)])
	return g,vc_approx_2(g)
	"""
	d = {}
	DFS(g,n2,d)
	print([str(x) + str(d[x]) for x in d.keys()])
	"""
if __name__ == '__main__':
	main()