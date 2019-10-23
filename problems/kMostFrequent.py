def kMostFrequent(arr_, k):
    freq = {}
    for element in arr_:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1

    inv_freq, max_count = {}, 0
    for elem, count in freq.items():
        if count in inv_freq:
            inv_freq[count].append(elem)
        else:
            inv_freq[count] = [elem]

        max_count = max(count, max_count)

    k_freq_elems = []
    for count in range(max_count, 0, -1):
        if count in inv_freq:
            k_freq_elems.extend(inv_freq[count])

        if len(k_freq_elems) == k:
            return k_freq_elems

        if len(k_freq_elems) > k:
            return None


if __name__ == '__main__':
    print(kMostFrequent([1,1,1,2,2,3], 2))
