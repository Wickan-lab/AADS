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

	x = g.insert_vertex('x')

	s = g.insert_vertex('s')

	y = g.insert_vertex('y')

	d = g.insert_vertex('d')
	e = g.insert_vertex('e')
	j = g.insert_vertex('j')
	k = g.insert_vertex('k')

	p = g.insert_vertex('p')
	q = g.insert_vertex('q')
	r = g.insert_vertex('r')
	g_ = g.insert_vertex('g_')
	e_ = g.insert_vertex('e_')

	n1 = g.insert_vertex('1')
	n2 = g.insert_vertex('2')
	n3 = g.insert_vertex('3')
	n4 = g.insert_vertex('4')
	n5 = g.insert_vertex('5')
	n6 = g.insert_vertex('6')











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

	#test 3

	z_x = g.insert_edge(z,x)

	x_h = g.insert_edge(x,h)	
	x_t = g.insert_edge(x,t)

	s_n = g.insert_edge(s,n)
	s_c = g.insert_edge(s,c)
	s_l = g.insert_edge(s,l)

	y_w = g.insert_edge(y,w)
	y_a = g.insert_edge(y,a)
	y_b = g.insert_edge(y,b)
	y_l = g.insert_edge(y,l)

	#test 4
	c_e = g.insert_edge(c,e)
	e_d = g.insert_edge(e,d)
	d_j = g.insert_edge(d,j)
	j_k = g.insert_edge(j,k)

	#test5
	p_x = g.insert_edge(p,x)
	p_q = g.insert_edge(p,q)
	q_x = g.insert_edge(q,x)
	q_r = g.insert_edge(q,r)
	q_g_ = g.insert_edge(q,g_)
	g__r  = g.insert_edge(g_,r)
	g__e = g.insert_edge(g_,e)
	e_e_ = g.insert_edge(e,e_)

	#test6
	w_n3 = g.insert_edge(w,n3)
	n3_n4 = g.insert_edge(n3,n4)
	n3_n1 = g.insert_edge(n3,n1)
	n3_n2 = g.insert_edge(n3,n2)
	
	n1_n2 = g.insert_edge(n1,n2)
	n1_n4 = g.insert_edge(n1,n4)

	n4_n2 = g.insert_edge(n4,n2)

	p_n5 = g.insert_edge(p,n5)
	n5_m = g.insert_edge(n5,m)
	m_n6 = g.insert_edge(m,n6)
	n6_u = g.insert_edge(n6,u)



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