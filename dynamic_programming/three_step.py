def three_step(num: int):

    ways = {0: 1}

    def count_ways(n: int):
        if n < 0:
            return 0
        elif n in ways:
            return ways[n]
        else:
            ways[n] = count_ways(n-1) + count_ways(n-2) + count_ways(n-3)
            return ways[n]

    return count_ways(num)


if __name__ == '__main__':
    print(three_step(10))
