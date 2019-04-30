class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def sort_stack(st: Stack) -> Stack:
    tempS, _len = Stack(), st.size()

    for i in range(_len):
        max = 0
        for _ in range(_len - i):
            elem = st.pop()

            if elem > max:
                tempS.push(max)
                max = elem
            else:
                tempS.push(elem)

        st.push(max)

        for _ in range(_len - i - 1):
            st.push(tempS.pop())

    return st


if __name__ == '__main__':
    st = Stack()
    st.push(100)
    st.push(3)
    st.push(5)
    st.push(4)
    sorted_st = sort_stack(st)

    for _ in range(sorted_st.size()):
        print(sorted_st.pop())
