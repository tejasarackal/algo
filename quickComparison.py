import numpy as np
from datetime import datetime as time


def find_median(arr):
    n = arr.size - 1
    new = np.array([arr[0], arr[n/2], arr[-1]])
    median = int(np.median(new))

    print(arr, new, median)
    for i in range(arr.size):
        if arr[i] == median:
            return i


def partition(arr):
    pivot = arr[0]
    i=1

    for j in range(1,arr.size):
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
    if i > 1:
        arr[0] = arr[i-1]
        arr[i-1] = pivot
        if i <= j:
            return arr[0:i-1], arr[i:j+1]
        else:
            return arr[0:j], None
    else:
        return None, arr[1:arr.size]


def quick_sort(arr, pick):
    count = 0
    if arr is None or arr.size <= 1:
        return arr, count
    elif pick == 0:
        pivot = arr[0]
        count = arr.size - 1
        left_partition, right_partition = partition(arr)
        left_partition, left_count = quick_sort(left_partition, pick)
        right_partition, right_count = quick_sort(right_partition, pick)
        count += left_count + right_count
    elif pick == 1:
        temp = arr[0]
        arr[0] = arr[-1]
        arr[-1] = temp

        pivot = arr[0]
        count = arr.size - 1
        left_partition, right_partition = partition(arr)
        left_partition, left_count = quick_sort(left_partition, pick)
        right_partition, right_count = quick_sort(right_partition, pick)
        count += left_count + right_count
    else:
        index = find_median(arr)
        temp = arr[0]
        arr[0] = arr[index]
        arr[index] = temp

        pivot = arr[0]
        count = arr.size - 1
        left_partition, right_partition = partition(arr)
        left_partition, left_count = quick_sort(left_partition, pick)
        right_partition, right_count = quick_sort(right_partition, pick)
        count += left_count + right_count

    if left_partition is None and right_partition is None:
        return arr, count
    elif left_partition is None:
        return np.concatenate((pivot, right_partition), axis=None), count
    elif right_partition is None:
        return np.concatenate((left_partition, pivot), axis=None), count
    return np.concatenate((left_partition, pivot, right_partition), axis=None), count


lines = np.loadtxt(fname="QuickArray.txt", dtype="int")
n = lines.size

#lines = np.array([11,12,9,10,1,2,3,4,5])
#arr1 = np.array(lines)
result, count = quick_sort(lines, 0.5)
print count

