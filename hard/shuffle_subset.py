import random


def shuffle_subset(A: list, m: int):
    subset = list()
    for index, elem in enumerate(A):
        choice = random.randint(index, len(A) - 1)
        subset.append(A[choice])
        A[index] = A[choice]
        A[choice] = elem

        if index >= m - 1:
            break;

    return subset


if __name__ == '__main__':
    print(shuffle_subset([i for i in range(100)], 10))
