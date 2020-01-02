from graph import *
from vertexcover import vc_approx_2

def main():
	g = Graph(directed=True)
	print(g.is_directed())
	u = g.insert_vertex('u')
	t = g.insert_vertex('t')
	v = g.insert_vertex('v')
	z = g.insert_vertex('z')
	f = g.insert_vertex('f')

	g.insert_edge(u,t)
	g.insert_edge(t,v)
	g.insert_edge(v,u)
	g.insert_edge(u,z)
	g.insert_edge(z,f)
	g.insert_edge(f,t)

	vc = vc_approx_2(g)
	print([str(x) for x in vc])

	"""
	w = g.insert_vertex('w')
	h = g.insert_vertex('h')
	a = g.insert_vertex('a')
	b = g.insert_vertex('b')
	c = g.insert_vertex('c')
	"""
if __name__ == '__main__':
	main()