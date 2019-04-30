# incomplete
from llist import sllist


def partition(ls: sllist, pivot: int):
    lt, gt = ls.first, ls.first.next

    while lt.next:
        lesser_found = False
        # find lesser than pivot element
        while gt.next:
            if gt.value < pivot:
                lesser_found = True
                break

        if lesser_found:
            return True

    return ls


if __name__ == '__main__':
    ls = sllist([1,2,3,4,5,6,7,2,3,4,4,10])
    print(partition(ls, 3))

