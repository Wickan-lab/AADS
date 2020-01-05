from tree import *
from sortedtablemap import *


class BTreeNode:

    # 1) root property: root has at least 2 and at most b children.
    # 2) node size property: each internal node, unless it is the root, has at least a and at most b children.
    # 3) depth property: all leaves have the same depth.

    def __init__(self, b):
        #create an empty tree
        #b = 2a = d
        self.firstMap = SortedTableMap
        self.secondMap = SortedTableMap
        self.firstMap.__init__()
        self.secondMap.__init__()
        self.b = b

    def element(self, x):
        """Return the element stored at this Key."""
        if x in self.firstMap.keys():
            return self.firstMap[x]

    def __eq__(self, other):
        """Return True if Keys are equal."""
        return self.firstMap.key == other.key 


class BTree(Tree):

    def __init__(self, b):
        self.root = BTreeNode(b)
        self.b = b

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return a Key representing the alberi's root (or None if empty)."""
        if self.firstMap.__len__() > 0:
            return self.firstMap[0].key
        else:
            return None

    def parent(self, p):
        """Return a Key representing p's parent (or None if p is root)."""
        if self.firstMap.__len__() > 1 :
            return self.firstMap[p-1].key
        else:
            return None

    def num_children(self, p):
        """Return the number of children that Key p has."""
        if self.firstMap[p].keys.__eq__(self.secondMap[p]):
            return len(self.secondMap[p])

    def children(self, p):
        """Generate an iteration of Keys representing p's children."""
        if self.firstMap[p].keys.__eq__(self.secondMap[p]):
            return self.secondMap[p]

    def __len__(self):
        """Return the total number of elements in the alberi."""
        return self.firstMap.keys().__len__()

    def search(self, k):
        """Return values of k"""
        if k in self.firstMap.keys():
            for k in self.firstMap.keys():
                print(self.firstMap[k])
                return self.firstMap[k]
        else:
            return None

    def check_root_property(self, b):
        if self.firstMap.__len__() < 1:
            pass
        else:
            if self.firstMap.__len__() in range (2 , b):
                return True
            else:
                return False

    def check_node_size_property(self, a, b ):
        if self.firstMap.__len__() < 1:
            pass
        if self.secondMap.__len__() in range(a, b):
            return True
        else:
            return False

    def check_depth_property(self):
        for k in self.firstMap.keys():
            if self.is_leaf():
                d = self.depth(k)
                break
        for k in self.firstMap.keys():
            if self.is_leaf():
                if self.depth(k).__ne__(d):
                    return False
        return True

    def insert(self, k, values):
        """insert a new node (new key in the map) """
        self.firstMap.__setitem__(k, values)
        #if (not(self.is_empty() and (self.check_depth_property() or self.check_root_property() or self.check_depth_property()))):

    #RIBILANCIA

    def delete(self, k, values):
        self.firstMap.__delitem__(k, values)
       # if (not(self.check_depth_property() or self.check_root_property() or self.check_depth_property())):
    #RIBILANCIA

    # def rebalance()

