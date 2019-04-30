MAX_BITS = 32
ALL_ONES = 2 ** (MAX_BITS + 1) - 1


def insertion(n: int, m: int, i: int, j: int):
    m <<= i

    left, right = ALL_ONES << j + 1, ALL_ONES >> MAX_BITS - i
    mask = left | right

    return (n & mask) | m


if __name__ == '__main__':
    print(bin(insertion(130, 5, 2, 4)))
