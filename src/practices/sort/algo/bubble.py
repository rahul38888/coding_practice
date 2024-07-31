def bubble_sort(array, length):
    is_swapper = True
    while is_swapper:
        is_swapper = False
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_swapper = True
    return array
