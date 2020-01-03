from sortedtablemap import SortedTableMap


class BTreeNode(object):
    """A B-Tree Node.

    attributes
    =====================

    leaf : boolean, determines whether this node is a leaf.
    elements : list, a list of keys internal to this node
    c : list, a list of children of this node
    firstmap : SortedTableMap, contains all the elements in the current node
    secondmap : SortedTableMap, contains all the elements of the current node's children

    """

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.elements = []
        self.c = []

    def __str__(self):
        if self.leaf:
            return "BTreeNode\n\tKeys:{0}\n\tChildren:{1}\n".format(self.elements, self.c) #LEAF
        else:
            return "BTreeNode with {0} keys, {1} children\n\tK:{2}\n\n".format(len(self.elements), len(self.c),     #INTERNAL
                                                                                        self.elements, self.c)


from sortedtablemap import SortedTableMap


class BTree(object):
    def __init__(self, d, c=None):        #d is the maximum degree
        self.root = BTreeNode(leaf=True)
        self.d = d
        self.c = []
        self.firstmap = SortedTableMap()
        self.secondmap = SortedTableMap()
        self.i = 1

    def search(self, k, x=None):  #DA MODIFICARE PER LE MAP
        """Search the B-Tree for the key k.

        args
        =====================
        k : Key to search for
        x : (optional) Node at which to begin search. Can be None, in which case the entire tree is searched.

        """
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.elements) and k > x.elements[i]:  # look for index of k
                i += 1
            if i < len(x.elements) and k == x.elements[i]:  # found exact match
                return (x, i)
            elif x.leaf:  # no match in keys, and is leaf ==> no match exists
                return None
            else:  # search children
                return self.search(k, x.c[i])
        else:  # no node provided, search root of tree
            return self.search(k, self.root)

    def insert(self, k):
        r = self.root

        if len(r.elements) == (2 * self.d) - 1:  # keys are full, so we must split
            s = BTreeNode()
            first = SortedTableMap()
            second = SortedTableMap()
            self.root = s
            first[self.i] = self.root.elements
            second[self.i] = self.root.c

            if self.i > 1:
                second[1] = self.root.elements

            s.c.insert(0, r)  # former root is now 0th child of new root s
            self._split_child(s, 0)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

        self.i += 1

    def _insert_nonfull(self, x, k):
        i = len(x.elements) - 1
        if x.leaf:
            # insert a key
            x.elements.append(0)
            while i >= 0 and k < x.elements[i]:
                x.elements[i + 1] = x.elements[i]
                i -= 1
            x.elements[i + 1] = k
        else:
            # insert a child
            while i >= 0 and k < x.elements[i]:
                i -= 1
            i += 1
            if len(x.c[i].elements) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.elements[i]:
                    i += 1
            self._insert_nonfull(x.c[i], k)

    def _split_child(self, x, i):
        d = self.t
        y = x.c[i]
        z = BTreeNode(leaf=y.leaf)

        # slide all children of x to the right and insert z at i+1.
        x.c.insert(i + 1, z)
        x.elements.insert(i, y.elements[t - 1])

        # keys of z are d to 2t - 1,
        # y is then 0 to t-2
        z.elements = y.elements[t:(2 * t - 1)]
        y.elements = y.elements[0:(t - 1)]

        # children of z are d to 2t els of y.c
        if not y.leaf:
            z.c = y.c[t:(2 * t)]
            y.c = y.c[0:(t - 1)]

    def __str__(self):
        r = self.root
        return r.__str__() + '\n'.join([child.__str__() for child in r.c])



