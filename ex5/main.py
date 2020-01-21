from graph import *

from vertexcover import *
import random
import time

def main():
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

	"""
	start_time = time.time()
	for g in graphs:
		vc(g)

	print("--- %s seconds to execute the algorithm (UNbounded)---" % (time.time() - start_time))
	"""

if __name__ == '__main__':
	main()
