from llist import sllist


def partition(ls: sllist, pivot: int):
    lt = ls.first

    while lt:
        temp = lt
        if lt.value < pivot and ls.first != lt:
            lt = temp.next
            ls.remove(temp)
            ls.appendleft(temp)
        else:
            lt = lt.next

    return ls


if __name__ == '__main__':
    ls = sllist([1,2,3,4,5,6,7,2,3,4,4])
    print(partition(ls, 1))

