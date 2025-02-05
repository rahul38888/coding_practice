from typing import List


def binary_search(arr: List[int], target: int):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]

    vals = [-1, 0, 3, 4, 8, 10]
    for v in vals:
        print(f"{v} in arr: {binary_search(arr, v)}")
