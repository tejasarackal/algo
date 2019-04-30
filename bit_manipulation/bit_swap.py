def bit_swap(num: int):
    return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)


if __name__ == '__main__':
    print(bit_swap(9))
