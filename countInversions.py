from numpy import loadtxt as lt, array, concatenate, sort, where
from datetime import datetime as time

lines = lt(fname="IntegerArray.txt", dtype="int")
n = lines.size

timer = dict()

def record_time(method):
    if method in timer:
        timer[method] = time.now() - timer[method]
    else:
        timer[method] = time.now()


def countInversions(A):
    if A.size <= 1:
        return A, 0
    else:
        half = A.size/2
        B, x = countInversions(A[0:half])
        C, y = countInversions(A[half:A.size])
        D, z = mergeSortCountSplit(A)
        return D, x + y + z


def mergeSortCountSplit(arr):

    count = 0
    if arr.size <= 1:
        return arr, 0
    i = 0
    j = 0
    half = arr.size/2

    A, cnt = mergeSortCountSplit(arr[0:half])
    B, cnt = mergeSortCountSplit(arr[half:arr.size + 1])
    C = array(arr.tolist())

    for k in range(arr.size):
        if i < A.size and j < B.size:
            if A[i] <= B[j]:
                C[k] = A[i]
                i += 1
            else:
                C[k] = B[j]
                j += 1
                count += (A.size - i)
        else:
            if i > A.size - 1:
                C[k] = B[j]
                j += 1
            else:
                C[k] = A[i]
                i += 1

    return C, count


def quickSortCountSplit(arr):

    if arr.size <= 1:
        return arr
    else:
        pivot = arr[0]
        left, right, num1 = partition(arr, pivot)
        sortedLeft, num2 = quickSortCountSplit(left)
        sortedRight, num3 = quickSortCountSplit(right)
        return concatenate((sortedLeft, pivot, sortedRight), axis=None), num1 + num2 + num3


def partition(arr, pivot):

    C = array(arr.tolist())

    i = 0
    j = arr.size - 1




def countInversionNaive(arr):

    count = 0
    new = sort(arr)

    min = new[arr.size - 1]
    minindex = arr.size - 1

    for i in range(0,arr.size):
        maxcheck = where(new == arr[i])

    return count


record_time('countInversions')
sortedArray, counter1 = countInversions(A=lines)
record_time('countInversions')

record_time('countInversionNaive')
counter2 = countInversionNaive(lines)
record_time('countInversionNaive')

print(lines)
print(counter1)
print(counter2)

for method in timer:
    print('Method - ' + method + ' , Time took - ' + str(timer[method]))