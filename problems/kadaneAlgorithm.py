# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

# Output:
# Print the maximum sum of the contiguous sub-array in a separate line for each test case.

# Constraints:
# 1 ≤ T ≤ 110
# 1 ≤ N ≤ 106
# -107 ≤ A[i] <= 107

# Example:
# Input
# 2
# 5
# 1 2 3 -2 5
# 4
# -1 -2 -3 -4
# Output
# 9
# -1


def kadaneAlgorithm(arr):
    sum_arr, m_sum = list(), 0

    for elem in arr:
        m_sum += elem
        sum_arr.append(m_sum)

    init_val = arr[0]
    g_max = m_sum = init_val

    for i, sum in enumerate(sum_arr):
        m_sum += arr[i]
        if 0 < i < len(sum_arr) - 1:
            if sum_arr[i - 1] > sum and sum < sum_arr[i + 1]: # local minima
                m_sum = max(sum, 0)
        g_max = max(g_max, m_sum)

    return g_max

if __name__ == '__main__':
    print(kadaneAlgorithm([-1, -2, -3, -4]))
