

def check_one_insert_away(long_str, short_str):
    mismatch = False
    index = 0

    for ch in short_str:
        if ch != long_str[index]:
            if not mismatch:
                mismatch = True
                index += 1
            else:
                return False

        index += 1

    return True


def check_one_replace_away(first_str, second_str):
    if len(first_str) == len(second_str):
        mismatch = False

        for index in range(len(first_str)):
            if first_str[index] != second_str[index]:
                if not mismatch:
                    mismatch = True
                else:
                    return False

        return True
    else:
        return False


def is_one_away(first_str, second_str):
    if isinstance(first_str, str) and isinstance(second_str, str):
        if len(first_str) == len(second_str):
            return check_one_replace_away(first_str, second_str)
        elif len(first_str) - len(second_str) == 1:
            return check_one_insert_away(long_str=first_str, short_str=second_str)
        elif len(second_str) - len(first_str) == 1:
            return check_one_insert_away(long_str=second_str, short_str=first_str)

    return False


if __name__ == '__main__':
    print(is_one_away("pales","palesa"))
