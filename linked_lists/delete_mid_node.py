from llist import sllist


def delete_mid_node(ls: sllist):
    last, mid = ls.first, ls.first

    while last.next and last.next.next:
        mid = mid.next
        last = last.next.next

    ls.remove(mid)

    return ls


if __name__ == '__main__':
    ls = sllist(['a'])
    delete_mid_node(ls)
    print(ls)
