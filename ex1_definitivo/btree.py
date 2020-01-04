from tree import *
from sortedtablemap import *


class BTreeNode:

    # 1) root property: la radice ha almeno 2 e al max b figli.
    # 2) node size property: ogni nodo interno (che non sia la radice) ha almeno a figli e al max b figli.
    # 3) depth property: tutte le foglie hanno la stessa profondità

    def __init__(self, b):
        "crea un albero vuoto"
        "b = 2a = d"
        self.firstMap = SortedTableMap
        self.secondMap = SortedTableMap
        self.firstMap.__init__()
        self.secondMap.__init__()
        self.b = b

    def element(self, x):  # (Position = Key)
        """Return the element stored at this Position ."""
        if x in self.firstMap.keys():
            return self.firstMap[x]

    def __eq__(self, other):
        """Return True if other Position represents the same location."""
        return self.firstMap.key == other.key  # compare items based on their keys


class BTree(Tree):

    def __init__(self, b):
        self.root = BTreeNode(b)
        self.b = b


    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the alberi's root (or None if empty)."""
        if self.firstMap.__len__() > 0:
            return self.firstMap[0].key
        else:
            return None

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        if self.firstMap.__len__() > 1 :
            return self.firstMap[p-1].key
        else:
            return None

    def num_children(self, p):
        """Return the number of children that Position p has."""
        if self.firstMap[p].keys.__eq__(self.secondMap[p]): #dubbio
            return len(self.secondMap[p])

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.firstMap[p].keys.__eq__(self.secondMap[p]):  # dubbio
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









