from llist import sllist


def return_kth_last(ls: sllist, k: int):
    kth, last = ls.first, ls.first

    # hop last k times ahead
    for _ in range(k):
        if last.next:
            last = last.next
        else:
            return None

    while last.next:
        kth = kth.next
        last = last.next

    return kth


if __name__ == '__main__':
    ls = sllist([1, 1, 2, 2, 5, 4, 4, 4, 5, 6])
    print(return_kth_last(ls, 10))
