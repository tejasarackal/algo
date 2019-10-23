def is_substring(a, b):
    return a in b


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return is_substring(s1, s2 + s2)


if __name__ == '__main__':
    print(string_rotation('abc', 'cba'))
