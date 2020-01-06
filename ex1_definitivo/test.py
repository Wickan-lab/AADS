from btree import *
from sortedtablemap import *

t = BTree(4).BTreeNode(None)
c = BTree(4).BTreeNode(t)
a = BTree(4).BTreeNode(t)
d = BTree(4).BTreeNode(c)
e = BTree(4).BTreeNode(c)
a[12] = 'pp'
a[15] = 'gg'

d[4] = 'ff'
d[5] = 'gjk'

c[3] = 'pcfg'
c[6] = d

e[7] = 'c'
e[8] = 'a'
c.toppa = e


t[10] = c
t[20] = a
t[30] = 'raf + giovanni'
t[40] = "ciao"
tree = BTree(4)

tree.root = t
print([str(x) for x in tree.children(tree.get_root())])
"""
#print(tree.num_children(t))
root = tree.get_root()
s = tree.search(t,10)
print(s)
print([str(x) for x in s])

#print([str(x) for x in t[2][1]])
"""
#sprint(tree.height())