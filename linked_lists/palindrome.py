from llist import sllist


def palindrome(ls: sllist) -> bool:
    ch_freq, _len = dict(), 0
    counter = ls.first

    while counter:
        ch_freq[_len] = counter.value
        _len, counter = _len + 1, counter.next

    for i in range(int((_len + 1) / 2)):
        if ch_freq[i] != ch_freq[_len - 1 - i]:
            return False

    return True


if __name__ == '__main__':
    ls = sllist(['a', 'b', 'd', 'a', 'b'])
    print(palindrome(ls))
