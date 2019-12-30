"""

let count be an integer
set count to 0
for each vertex v in V’
	remove all edges adjacent to v from set E
	increment count by 1
if count = k and E is empty then
	the given solution is correct
else
	the given solution is wrong

cioè se hai rimosso tutti gli edge incidenti per ogni vertice e quando hai finito non ci sono più edge

"""

#UGLY test the output of vertex cover


from vertexcover import *
from main import main

def remove_edges(gc,v):
	print('Vertex v : ' + str(v))
	found = False
	#find v
	for ver in gc._outgoing:
		if ver.element() == v.element():
			v = ver
			found = True
	if not found:
		exit()

	remove_edges = gc.incident_edges(v)
	covered_vert = [e.opposite(v) for e in remove_edges]
	
	for elem in covered_vert:
		del gc._outgoing[elem][v]
		if gc._outgoing[elem] is None:
			del gc._outgoing[elem]

	del gc._outgoing[v]

count = 0

g,v_dash = main()

for v in v_dash:
	remove_edges(g,v)
	count += 1
if count == len(v_dash) and not g.edges():
	print('Correct solution')
else:
	print('Wrong solution')



