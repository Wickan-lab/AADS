class BTree(object):

  class Node(object):

    def __init__(self, b):
      self.keys = []
      self.children = []
      self.is_leaf = True
      self._b = b

    def _find_index(self, k, low, high, node):
        if high < low:
            return low
        else:
            mid = (low + high) // 2

            if k == node.keys[mid]:
                return mid
            elif k < node.keys[mid]:
                return self._find_index(k, 0, mid - 1, node)
            else:
                return self._find_index(k, mid + 1, high, node)

    def split(self, parent, key):
      new_node = self.__class__(self._b)

      mid = self.size()//2
      split_value = self.keys[mid]
      parent.add_key(split_value)

      new_node.children = self.children[mid + 1:]
      self.children = self.children[:mid + 1]
      new_node.keys = self.keys[mid+1:]
      self.keys = self.keys[:mid]

      if len(new_node.children) > 0:
        new_node.is_leaf = False

      parent.children = parent.add_child(new_node)
      if key < split_value:
        return self
      else:
        return new_node

    def _is_full(self):
      return self.size() == 2 * self._b - 1

    def size(self):
      return len(self.keys)

    def add_key(self, value):
      self.keys.append(value)
      self.keys.sort()

    def add_child(self, new_node):
      i = len(self.children) - 1
      while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
        i -= 1
      return self.children[:i + 1]+ [new_node] + self.children[i + 1:]


  def __init__(self, b):
    self._b = b
    if self._b <= 1:
      raise ValueError("b has to be 2 or more.")
    self.root = self.Node(b)

  def insert(self, key):
    node = self.root
    if node._is_full():
      new_root = self.Node(self._b)
      new_root.children.append(self.root)
      new_root.is_leaf = False
      node = node.split(new_root, key)
      self.root = new_root

    while not node.is_leaf:

      i = self._find_index(key, 0, self.size() - 1, node)
      next = node.children[i]

      if next._is_full():
        node = next.split(node, key)
      else:
        node = next
    node.add_key(key)

  def search(self, value, node=None):
    if node is None:
      node = self.root
    if value in node.keys:
      return True
    elif node.is_leaf:
      return False
    else:
      i = 0
      i = self._find_index(value, 0, self.size() - 1, node)      
      return self.search(value, node.children[i])

  def print_order(self):
    this_level = [self.root]
    while this_level:
      next_level = []
      output = ""
      for node in this_level:
        if node.children:
          next_level.extend(node.children)
        output += str(node.keys) + " "
      print(output)
      this_level = next_level
