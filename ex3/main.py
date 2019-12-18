from graph import *
from dfs import *

def main():
	g = Graph()

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
	#a_b = g.insert_edge(a,b)

	

	#print([(str(x),str(x.endpoints()[0])) for x in g.edges()])

	iterative_dfs(g,u,DEBUG=True)












if __name__ == '__main__':
	main()