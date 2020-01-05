from tree import *
from sortedtablemap import *


class BTreeNode(Tree):

    # 1) root property: la radice ha almeno 2 e al max b figli.
    # 2) node size property: ogni nodo interno (che non sia la radice) ha almeno a figli e al max b figli.
    # 3) depth property: tutte le foglie hanno la stessa profondità


    def __init__(self):
        self.firstMap = SortedTableMap
        self.firstMap.Item.key = []
        self.firstMap.Item.value = []



    def element(self, x):
        """Return the element stored at this Position ."""
        if x in self.firstMap.Item.key:
            return self.firstMap.Item.key[x]


    def __eq__(self, other):
        """Return True if other Position represents the same location."""
        return (self == other)


class BTree(Tree):

    def __init__(self, b):
        self.root = BTreeNode()
        self.b = b
        self.firstMap = SortedTableMap()
        self.listMap = SortedTableMap()
        self.listMap = []



    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        if self.listMap[0].__len__() > 0:
            return self.listMap[0].key
        else:
            return None

    def parent(self, k):    #DA MODIFICARE
        if self.firstMap.__len__() > 1 :
            return self.firstMap.Item.key[k-1]
        else:
            return None

    def num_children(self, p):
        return self.listMap[p].values().__len__()

    def children(self, p):
        return self.listMap[p].values()

    def __len__(self):
        return self.listMap.__len__()


    def search(self, k):
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









