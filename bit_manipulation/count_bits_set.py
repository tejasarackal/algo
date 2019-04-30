def count_bits_set(num: int) -> int:
    return bin(num).count('1')


def rotate_bits(num: int, rot: int) -> int:
    b, sig = bin(num)[2:], bin(num)[:2]
    l = len(b)

    print(f'{sig}{b[l - rot:]}{b[:l - rot]}')
    return int(f'{sig}{b[l - rot:]}{b[:l - rot]}', 2)


def rotate_bits(num: int, rot: int) -> int:
    return num << rot | num >> (32 - rot)


def is_off_by_one_bit(num1: int, num2: int) -> bool:
    diff = num1 ^ num2
    return diff & (diff - 1) == 0


def add(num1: int, num2: int) -> int:
    sum, carry = num2, num1

    while carry != 0:
        sum, carry = sum ^ carry, (sum & carry) << 1

    return sum


if __name__ == '__main__':
    print(add(2, 1))
