def selection_sort(array, length):
    start = 0
    for i in range(length):
        temp_min = start
        if start == length - 1:
            break
        for j in range(start + 1, length):
            if array[temp_min] > array[j]:
                array[temp_min], array[j] = array[j], array[temp_min]
        start += 1

    return array
