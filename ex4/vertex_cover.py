class Tree(object):
    "Generic tree node."

    def __init__(self, name='root', children=None, parent=None, software=0):
        self.name = name
        self.parent = parent
        self.software = software
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.name) + repr(self.software) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def add_child(self, node):
        assert isinstance(node, Tree)
        node.parent = self.name
        self.children.append(node)

    # def is_leaf(self):

    def height(self):
        count = 0
        if self.children.__len__() == 0:
            return count
        else:
            for child in self.children:
                v = child.height()
                if v > count:
                    count = v
            return count + 1

    def is_root(self):
        return self.parent == None

    def is_leaf(self):
        return self.children.__len__() == 0

    def num_children(self):
        return len(self.children)

    def give_software(self):
        count = 0
        print("I'm inside: " + self.name)
        # // The size of minimum vertex cover is zero
        # //  if tree is empty or there is only one node
        if self.is_root() and self.num_children() == 0:
            count += 1
            self.software = 1
        elif self.height() == 1:
            count += 1
            self.software = 1
            return count

        # // If vertex cover for this node is
        # // already evaluated, then return it
        # // to save recomputation of same subproblem again.
        elif self.height() > 1 and not self.is_root():
            count += 1
            self.software = 1

        for c in self.children:
            count += c.give_software()
        return count


dile = Tree("Dile")
edo = Tree("Edo")
raffo = Tree("Raffo", [dile, edo])
cami = Tree("Cami")
stella = Tree("Stella", [Tree("Jess")])
gabry = Tree("Gabry", [Tree("Saba"), Tree("Luca"), stella])
ale = Tree("Ale", [Tree("Dave"), gabry])
fede = Tree("Fede", [ale, Tree("Fra")])

cami.add_child(raffo)
cami.add_child(fede)
peppe = Tree("Peppe", [Tree("Marco"), Tree("Gio"), Tree("Marghe")])
cami.add_child(peppe)
print(cami)
print("\n")

print(cami.give_software())
print(cami)