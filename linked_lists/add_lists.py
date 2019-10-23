from llist import sllist


def add_lists(list1: sllist, list2: sllist) -> sllist:
    counter1, counter2, carry = list1.first, list2.first, 0

    while counter1 and counter2:
        counter1.value += counter2.value + carry
        carry = counter1.value // 10
        counter1.value %= 10

        counter1 = counter1.next
        counter2 = counter2.next

    while counter1:
        if carry == 0:
            break
        counter1.value += carry
        carry = counter1.value // 10
        counter1.value %= 10
        counter1 = counter1.next

    while counter2:
        if carry == 0:
            list1.appendright(counter2.value)
        else:
            sum = counter2.value + carry
            list1.appendright(sum % 10)
            carry = sum // 10
        counter2 = counter2.next

    if carry == 1:
        list1.appendright(carry)

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
        carry = add // 10
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
    ls1, ls2 = sllist([4,5,4]), sllist([5,6,6])
    print(f'{ls1} + {ls2} = {add_list_reversed(ls1, ls2)}')
