class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def printList(self):
        next = self.root
        printStr = ''
        while next:
            printStr += str(next.data) + '->'
            next = next.next

        print(printStr[:-2])


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
    l.printList()

    d.next = Node('e')
    d.next.next = Node('f')

    l.printList()
