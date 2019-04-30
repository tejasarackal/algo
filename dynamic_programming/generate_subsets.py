def generate_subsets(_set: set):

    _subset = set()
    for i in _set:
        _subset.add({i})
        for j in _subset:
            j.add(i)

    return _subset


if __name__ == '__main__':
    print(generate_subsets({1,2,3}))
