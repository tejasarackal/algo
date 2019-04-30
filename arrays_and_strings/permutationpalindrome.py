

def create_char_freq_dist(istring):
    freq = {}
    for ch in istring:
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    return freq


def is_max_one_odd(freq):
    max_one = 0
    for k in freq:
        if freq[k] % 2 == 1 and max_one == 1:
            return False
        elif freq[k] % 2 == 1:
            max_one = 1
        else:
            pass
    return True


def is_permutation_palindrome(istring):
    if isinstance(istring, str):
        char_freq_dict = create_char_freq_dist(istring)
        return is_max_one_odd(char_freq_dict)
    return False


if __name__ == '__main__':
    print(is_permutation_palindrome("popoy e"))
