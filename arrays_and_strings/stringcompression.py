def count_compression(txt):
    count = 0
    prevch = ''

    for ch in txt:
        if prevch != ch:
            count += 2
        prevch = ch
    return count


def string_compression(txt):
    prevfreq, prevch = -1, ''
    compressedstr = []

    if count_compression(txt) >= len(txt):
        return txt

    for currentch in txt:
        if prevch == currentch:
            prevfreq += 1
        else:
            if prevfreq != -1:
                compressedstr.append(prevch)
                compressedstr.append(str(prevfreq))
            prevch = currentch
            prevfreq = 1
    compressedstr.append(prevch)
    compressedstr.append(str(prevfreq))

    if len(compressedstr) >= len(txt):
        return txt
    else:
        return ''.join(compressedstr)


if __name__ == '__main__':
    print(string_compression('aabbccddd'))
    print(string_compression('aabbccdd'))
    print(string_compression('abcd'))
