def toggle_bit(num: int, bit: int):
    if num >> bit & 1 == 1:
        return num & (((1 << num.bit_length()) - 1) & ~(1 << bit))
    else:
        return num | (1 << bit)


def swap(num: int, bit1: int, bit2: int):
    orig = num

    num = toggle_bit(num, bit1)
    num = toggle_bit(num, bit2)
    print(bin(orig), bit1, bit2, bin(num))

    return num


def next_numbers(num: int):
    # find first 0 - z
    # find next 1 - o
    # swap bits z, o to get min

    orig = num
    z, o = -1, -1

    while num > 0:
        o += 1
        if num & 1 == 0 and num & 2 == 2:
            break
        num >>= 1

    prev_next = swap(orig, o, o + 1)

    num = orig
    while num > 0:
        z += 1
        if num & 1 == 1 and num & 2 == 0:
            break
        num >>= 1
    fwd_next = swap(orig, z, z + 1)

    return prev_next, fwd_next


if __name__ == '__main__':
    print(next_numbers(1 + 8))
