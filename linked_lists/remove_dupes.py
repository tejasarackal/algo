from llist import sllist


def remove_dupes(unordered_ls: sllist):
    cur = unordered_ls.first
    val_set = {cur.value}

    while cur.next:
        if cur.next.value in val_set:
            unordered_ls.remove(cur.next)
        else:
            val_set.add(cur.next.value)
            cur = cur.next

    return unordered_ls


if __name__ == '__main__':
    unsorted = sllist([1,1,2,2,5,4,4,4,5,6])
    print(remove_dupes(unsorted))
