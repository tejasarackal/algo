def flip_bit_max(num: int):

    _len, _prev_len, orig, _max = 0, 0, num, -1
    while num > 0:
        if num & 1 == 1:
            _len += 1
        else:
            _prev_len = _len if num & 2 == 2 else 0
            _len = 0

        _max = _prev_len + _len + 1 if _prev_len + _len + 1 > _max else _max
        num >>= 1

    print(bin(orig), _max)
    return _max


if __name__ == '__main__':
    flip_bit_max(4 + 1 )
