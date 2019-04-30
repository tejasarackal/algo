def print_binary(num: float) -> int:
    if not 0 < num < 1:
        return -1

    b = []
    while num > 0 and len(b) < 32:
        num *= 2

        if num >= 1:
            b.append('1')
            num -= 1.0
        else:
            b.append('0')

    if len(b) == 32:
        print('ERROR')
    else:
        print(''.join(b))


if __name__ == '__main__':
    print_binary(0.5 + 0.125 + 0.0625 + 0.015625)
