from llist import sllist


def delete_mid_node(ls: sllist):
    last, mid = ls.first, ls.first

    while last.next and last.next.next and last.next.next.next:
        mid = mid.next
        last = last.next.next

    #mid.next = mid.next.next
    if mid.next and mid.next.next:
        ls.remove(mid.next)

    return ls


if __name__ == '__main__':
    ls = sllist(['a','b','c'])
    delete_mid_node(ls)
    print(ls)
