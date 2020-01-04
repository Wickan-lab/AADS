class TreeNode(object):
    "Generic tree node."

    def __init__(self, name, children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.name) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def add_child(self, node):
        assert isinstance(node, TreeNode)
        self.children.append(node)

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

    def degree(self):
        return len(self.children)

    def give_software(self, count=0):
        d = {}
        d[self.name] = False

        if count != 0:
            return count

        size_in = 1
        size_ex = 0
        d_in = {}
        d_ex = {}

        for c in self.children:
            (x, dic) = c.give_software(count)
            size_in += x
            d_in.update(dic)

            size_ex += 1

            for j in range(0, c.degree()):
                (x, dic) = c.children[j].give_software(count)
                size_ex += x
                d_ex.update(dic)

        count = min(size_in, size_ex)
        if size_in <= size_ex:
            d[self.name] = True
            d.update(d_in)
        else:
            for c in self.children:
                d[c.name] = True
                d.update(d_ex)
        return (count, d)