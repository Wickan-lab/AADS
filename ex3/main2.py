from graph import *
from dfs import *


def main():
	g = Graph()
	
	u = g.insert_vertex('u')
	m = g.insert_vertex('m')
	"""
	
	
	t = g.insert_vertex('t')
	y = g.insert_vertex('y')
	s = g.insert_vertex('s')
	w = g.insert_vertex('w')

	u_t = g.insert_edge(u,t)
	t_s = g.insert_edge(t,s)
	s_g = g.insert_edge(s,w)
	t_y = g.insert_edge(t,y)
	
	m_s = g.insert_edge(m,s)
	"""
	#u_m = g.insert_edge(u,m)
	#m_u = u_m = g.insert_edge(m,u)

	iterative_dfs(g,u)









if __name__ == '__main__':
	main()