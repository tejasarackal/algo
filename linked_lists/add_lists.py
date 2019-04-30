from llist import sllist


def add_lists(list1: sllist, list2: sllist) -> sllist:
    counter1, counter2, carry = list1.first, list2.first, 0

    while counter1 and counter2:
        counter1.value += counter2.value + carry
        carry = int(counter1.value / 10)
        counter1.value %= 10

        counter1 = counter1.next
        counter2 = counter2.next

    if counter1 and carry == 1:
        counter1.value += 1

    while counter2:
        list1.appendright(counter2.value + carry)
        carry = 0
        counter2 = counter2.next

    return list1


def add_list_reversed(list1: sllist, list2: sllist) -> sllist:
    st1, st2, st3 = [], [], []
    counter1, counter2, carry = list1.first, list2.first, 0
    flist = sllist()

    while counter1:
        st1.append(counter1.value)
        counter1 = counter1.next

    while counter2:
        st2.append(counter2.value)
        counter2 = counter2.next

    while st1 and st2:
        add = st1.pop() + st2.pop() + carry
        carry = int(add / 10)
        add %= 10

        st3.append(add)

    while st1:
        st3.append(st1.pop() + carry)
        carry = 0

    while st2:
        st3.append(st2.pop() + carry)
        carry = 0

    if carry == 1:
        flist.appendright(1)

    while st3:
        flist.appendright(st3.pop())

    return flist


if __name__ == '__main__':
    ls1, ls2 = sllist([7,2]), sllist([1,2,5])
    print(add_list_reversed(ls1, ls2))
