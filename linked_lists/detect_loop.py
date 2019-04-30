from llist import sllist


def detect_loop(ls: sllist) -> str:
    ch_freq = dict()
    cur = ls.first

    while cur:
        if cur.value in ch_freq:
            return cur.value
        else:
            ch_freq[cur.value] = True
            cur = cur.next

    return 'loop not found'


if __name__ == '__main__':
    print(detect_loop(ls= sllist(['A', 'B', 'C', 'D', 'E', 'C'])))
