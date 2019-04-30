

def replace_spaces(ch):
    if ch == ' ':
        return '%20'
    else:
        return ch


def urlify(istring, truelength):
    if isinstance(istring, str) and isinstance(truelength, int):
        istring = ''.join(map(replace_spaces, istring[0:truelength]))

    return istring


if __name__ == '__main__':
    print(urlify("123456", 5))
