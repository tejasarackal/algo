

def sparse_search(searchElem, ls, first, last):
    mid = int((first + last) / 2)
    print(first, mid, last)

    if ls[mid] == '':
        left, right = mid - 1, mid + 1
        while left >= first and right <= last:
            if ls[left] != '':
                mid = left
                break
            elif ls[right] != '':
                mid = right
                break
            else:
                left -= 1
                right += 1

        if ls[mid] == '':
            return -1

    if searchElem == ls[mid]:
        return mid
    elif searchElem < ls[mid]:
        return sparse_search(searchElem, ls, first, mid - 1)
    else:
        return sparse_search(searchElem, ls, mid + 1, last)


def search(searchElem, ls):
    if searchElem is None or searchElem == '':
        return -1
    else:
        return sparse_search(searchElem, ls, 0, len(ls) - 1)


if  __name__ == '__main__':
    ls = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '', '', 'end', '']
    print(search('end', ls))