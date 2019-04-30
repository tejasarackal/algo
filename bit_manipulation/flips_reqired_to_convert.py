def flips_required_to_convert(num1: int, num2: int):
    return bin(num1 ^ num2).count('1')


if __name__ == '__main__':
    print(flips_required_to_convert(29,1))
