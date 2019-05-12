class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def __str__(self):
        next = self.root
        printStr = ''
        while next:
            printStr += str(next.data) + '->'
            next = next.next

        if len(printStr) > 2:
            return printStr[:-2]
        else:
            return printStr


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    root = a
    a.next = b
    b.next = c
    c.next = d

    l = LinkedList()
    l.root = root
    print(l)

    d.next = Node('e')
    d.next.next = Node('f')

    print(l)