import math, sys


def peaks_and_valleys(ls: list):
    for mid_index in [2*i + 1 for i in range(math.ceil((len(ls) - 1)/2))]:
        peak_index, peak_elem = find_peak(ls, mid_index - 1, mid_index, mid_index + 1)
        if peak_index != mid_index:
            mid_elem = ls[mid_index]
            ls[mid_index] = peak_elem
            ls[peak_index] = mid_elem
    return ls


def find_peak(ls: list, a: int, b: int, c: int):
    elem_a = ls[a] if a < len(ls) else -sys.maxsize - 1
    elem_b = ls[b] if b < len(ls) else -sys.maxsize - 1
    elem_c = ls[c] if c < len(ls) else -sys.maxsize - 1

    max_elem = max(elem_a, elem_b, elem_c)
    if elem_a == max_elem:
        return a, elem_a
    elif elem_b == max_elem:
        return b, elem_b
    else:
        return c, elem_c


if __name__ == '__main__':
    print(peaks_and_valleys([i for i in range(100)]))
