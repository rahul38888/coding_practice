from math import floor


def sort_and_merge(array, s, e):
    if s >= e:
        return
    mid = floor((s + e) / 2)
    sort_and_merge(array, s, mid)
    sort_and_merge(array, mid + 1, e)

    i, j = 0, 0
    k = s
    arr1 = array[s:mid + 1]
    arr2 = array[mid + 1:e + 1]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            array[k] = arr1[i]
            i += 1
        else:
            array[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        array[k] = arr1[i]
        k += 1
        i += 1

    while j < len(arr2):
        array[k] = arr2[j]
        k += 1
        j += 1


def merge_sort(array, length):
    sort_and_merge(array, 0, length - 1)
    return array
