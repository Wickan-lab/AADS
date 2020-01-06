from btree import *
from sortedtablemap import *

t = BTree(4).BTreeNode(None)
c = BTree(4).BTreeNode(t)
a = BTree(4).BTreeNode(t)
d = BTree(4).BTreeNode(c)
e = BTree(4).BTreeNode(c)
a[12] = None
a[15] = None

d[4] = None
d[5] = None

c[3] = None
c[6] = d

e[7] = None
e[8] = None
c.toppa = e


t[10] = c
t[20] = a
t[30] = None
t[40] = None
tree = BTree(4)

tree.root = t
"""
#print(tree.num_children(t))
root = tree.get_root()
s = tree.search(t,10)
print(s)
print([str(x) for x in s])

#print([str(x) for x in t[2][1]])
"""
#print([str(x) for x in tree.children(tree.get_root())])
print(tree.height())
print(tree.check_depth_property())