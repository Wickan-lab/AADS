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
	l = g.insert_vertex('l')	
	m = g.insert_vertex('m')
	n = g.insert_vertex('n')
	

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
	#test 1
	c_u = g.insert_edge(c,u)
	w_l = g.insert_edge(w,l)
	l_f = g.insert_edge(l,f)
	#test 2
	a_b = g.insert_edge(a,b)
	b_l = g.insert_edge(b,l)
	l_c = g.insert_edge(l,c)
	v_m = g.insert_edge(v,m)
	m_n = g.insert_edge(m,n)
	n_h = g.insert_edge(n,h)
	n_l = g.insert_edge(n,l)
	"""	
	a_b = g.insert_edge(a,b)
	b_f = g.insert_edge(b,f)
	

	a_l = g.insert_edge(a,l)
	m_l = g.insert_edge(m,l)
	m_d = g.insert_edge(m,d)
	d_b = g.insert_edge(d,b)
	"""	
	iterative_dfs(g,z)












if __name__ == '__main__':
	main()