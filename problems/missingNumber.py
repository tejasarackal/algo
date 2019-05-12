# Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

# Input:
# The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

# Output:
# Print the missing number in array.

# Constraints:
# 1 ≤ T ≤ 200
# 1 ≤ N ≤ 107
# 1 ≤ C[i] ≤ 107

# Example:
# Input:
# 2
# 5
# 1 2 3 5
# 10
# 1 2 3 4 5 6 7 8 10

# Output:
# 4
# 9

import math

def missingNumber(arr):
    len_ = len(arr) + 1

    i, j, n_child = 0, len_ - 2,  math.floor(len_ / 2)
    while n_child > 0:
        if arr[i + n_child - 1] == i + n_child:
            i = i + n_child
        else:
            j = i + n_child - 1

        n_child = math.floor(n_child / 2)

    return j + 1 if j == 0 or arr[j - 1] == j else j


if __name__ == '__main__':
    print(missingNumber([2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(missingNumber([1, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(missingNumber([1, 2, 4, 5, 6, 7, 8, 9, 10]))
    print(missingNumber([1, 2, 3, 5, 6, 7, 8, 9, 10]))
    print(missingNumber([1, 2, 3, 4, 6, 7, 8, 9, 10]))
    print(missingNumber([1, 2, 3, 4, 5, 7, 8, 9, 10]))
    print(missingNumber([1, 2, 3, 4, 5, 6, 8, 9, 10]))
    print(missingNumber([1, 2, 3, 4, 5, 6, 7, 9, 10]))
    print(missingNumber([1, 2, 3, 4, 5, 6, 7, 8, 10]))

    print()
    print(missingNumber([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(missingNumber([1, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(missingNumber([1, 2, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(missingNumber([1, 2, 3, 5, 6, 7, 8, 9, 10, 11]))
    print(missingNumber([1, 2, 3, 4, 6, 7, 8, 9, 10, 11]))
    print(missingNumber([1, 2, 3, 4, 5, 7, 8, 9, 10, 11]))
    print(missingNumber([1, 2, 3, 4, 5, 6, 8, 9, 10, 11]))
    print(missingNumber([1, 2, 3, 4, 5, 6, 7, 9, 10, 11]))
    print(missingNumber([1, 2, 3, 4, 5, 6, 7, 8, 10, 11]))
    print(missingNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))
