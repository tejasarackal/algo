

def add_without_plus(num1: int, num2: int):

    while num2 != 0:

        addition = num1 ^ num2
        carry = (num1 & num2) << 1

        num1 = addition
        num2 = carry

    return num1


def rec_add_without_plus(num1: int, num2: int):
    if num2 == 0:
        return num1
    else:
        addition = num1 ^ num2
        carry = (num1 & num2) << 1
        return rec_add_without_plus(addition, carry)


if __name__ == '__main__':
    print(add_without_plus(210138489723987493178478913749813904, 231673478172948712748712874809128947981284091))
