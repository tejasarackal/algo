def magic_index(arr: list):

    def find_magic_index(arr: list, start: int, end: int):
        if end < start:
            return -1

        mid = int((start + end)/2)
        if arr[mid] == mid:
            return mid

        left_index = min(mid - 1, arr[mid])
        left = find_magic_index(arr, start, left_index)
        if left >= 0:
            return left

        right_index = max(mid + 1, arr[mid])
        right = find_magic_index(arr, right_index, end)
        if right >= 0:
            return right

        return -1

    return find_magic_index(arr, start=0, end=len(arr) - 1)


if __name__ == '__main__':
    print(magic_index([1,2,3,4,5,5]))
