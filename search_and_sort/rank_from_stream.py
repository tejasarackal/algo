

class RankNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.left_size = 0

    def insert(self, data):
        if data <= self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = RankNode(data)
            self.left_size += 1
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = RankNode(data)

    def getRank(self, data):
        if data == self.data:
            return self.left_size
        elif data < self.data:
            if self.left is None:
                return -1
            else:
                return self.left.getRank(data)
        elif data > self.data:

            if self.right is None:
                return -1
            else:
                right_rank = self.right.getRank(data)
                if right_rank == -1:
                    return -1
                else:
                    return self.left_size + 1 + right_rank


if __name__ == '__main__':
    root = RankNode(5)
    root.insert(1)
    root.insert(4)
    root.insert(4)
    root.insert(5)
    root.insert(9)
    root.insert(7)
    root.insert(13)
    root.insert(3)

    print(1, root.getRank(1))
    print(3, root.getRank(3))
    print(4, root.getRank(4))
    print(100, root.getRank(100))
