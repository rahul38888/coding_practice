

def find_in_rotated_sort(arr: list[int], target: int):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end)//2

        if arr[mid] == target:
            return arr[mid]

        if arr[start] <= arr[mid]:
            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return None


if __name__ == '__main__':
    array = [7, 8, 9, 1, 2, 3, 3, 4, 5, 6]

    vals = [7, 6, 9, 1, 8, 3, 4, 10, 0]

    for v in vals:
        print(f"{v} in arr: {find_in_rotated_sort(array, v)}")
