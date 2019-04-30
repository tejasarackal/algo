class Stack:
    def __init__(self):
        self.items = []
        self.mins = None

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

        if not self.mins and type(item) == int:
            self.mins = [item]
        elif type(item) == int:
            last_min = self.mins[-1]
            if last_min > item:
                self.mins.append(item)
            else:
                self.mins.append(last_min)

    def pop(self):
        self.mins.pop()
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def min(self):
        return self.mins[-1]


if __name__ == '__main__':
    st = Stack()
    st.push(8)
    st.push(17)
    st.push(19)
    st.push('1')
    st.push(2)
    st.push(7)
    print(st.min())
    st.pop()
    st.pop()
    print(st.min())