class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.root = None

    def printList(self):
        next = self.root
        printStr = ''
        while next:
            printStr += str(next.data) + '<-->'
            next = next.next

        if len(printStr) > 4:
            print(printStr[:-4])

    def push(self, node_):
        if self.root:
            node_.next = self.root
            self.root.prev = node_
            self.root = node_
        else:
            self.root = node_

    def append(self, node_):
        if self.root:
            next = self.root
            while next.next:
                next = next.next
            prevLast = next

            prevLast.next = node_
            node_.prev = prevLast
        else:
            self.root = node_

    def insertAfter(self, prevNode, node_):

        if prevNode is None:
            print('This node has no name')
            return

        if prevNode.next is None:
            prevNode.next = node_
            node_.prev = prevNode
        else:
            nextNode = prevNode.next
            prevNode.next  = node_
            node_.next = nextNode

            nextNode.prev = node_
            node_.prev = prevNode

    def insertBefore(self, nextNode, node_):

        if nextNode is None:
            print('This node has no name')
            return

        if nextNode.prev is None:
            self.push(node_)
        else:
            prevNode = nextNode.prev
            prevNode.next = node_
            node_.next = nextNode

            nextNode.prev = node_
            node_.prev = prevNode

    def deleteNode(self, node_):
        if node_ is None:
            print('A node has no name')
            return

        if node_.prev is None and node_.next is None and node_ == self.root:
            self.root = None
        elif node_.prev is None and node_.next is None:
            print('Abandoned node')
            return
        elif node_.prev is None and node_ == self.root:
            self.root = node_.next
            self.root.prev = None
        elif node_.next is None:
            prevNode = node_.prev
            node_.prev = None
            prevNode.next = None
        else:
            prevNode = node_.prev
            nextNode = node_.next

            node_.next = None
            node_.prev = None

            prevNode.next = nextNode
            nextNode.prev = prevNode


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.push(Node('c'))
    d.push(Node('b'))
    a = Node('a')
    d.push(a)

    d.printList()

    d.deleteNode(a)
    d.printList()

    dd = Node('d')
    d.append(dd)
    d.append(Node('e'))
    d.push(a)

    d.printList()
    d.deleteNode(dd)

    d.printList()
    d.deleteNode()

