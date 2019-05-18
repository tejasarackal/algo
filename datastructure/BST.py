class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def put(self, node):
        if node.key > self.key:
            if self.right:
                self.right.put(node)
            else:
                self.right = node
        elif node.key < self.key:
            if self.left:
                self.left.put(node)
            else:
                self.left = node
        else:
            self.value = node.value

    def search(self, key):
        if self.key == key:
            return self.value
        elif key > self.key:
            if self.right:
                return self.right.search(key)
            else:
                return None
        else:
            if self.left:
                return self.left.search(key)
            else:
                return None

    def __str__(self):
        str_ = ''

        if self.left:
            str_ += str(self.left) + ' <- '
        str_ += str(self.key) + ':' + str(self.value)
        if self.right:
            str_ += ' -> ' + str(self.right)

        return str_


class BST:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        node_ = BSTNode(key, value)
        if self.root:
            self.root.put(node_)
        else:
            self.root = node_

    def search(self, key):
        return self.root.search(key)

    def __str__(self):
        if self.root:
            return str(self.root)
        return 'Empty Tree'


if __name__ == '__main__':
    tree = BST()
    print(tree)

    tree.put(5, 'E')
    print(tree)

    tree.put(2, 'B')
    tree.put(7, 'G')
    tree.put(1, 'A')
    tree.put(3, 'C')
    print(tree)

    tree.put(4, 'D')
    tree.put(6, 'F')
    tree.put(8, 'H')
    tree.put(9, 'i')
    tree.put(10, 'J')
    print(tree)

    tree.put(9, 'I')
    print(tree)

    print(tree.search(9))
