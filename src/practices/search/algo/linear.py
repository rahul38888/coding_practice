def linear_search(arr, l, val):
    for i in range(l):
        if arr[i] == val:
            return i
    return -1