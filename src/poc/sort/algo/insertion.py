def insertion_sort(array, length):
    for i in range(1, length):
        for j in range(i):
            if (j == 0 and array[i] < array[j]) or (array[j-1] < array[i] < array[j]):
                temp_val = array[i]
                for k in range(j, i+1):
                    array[k], temp_val = temp_val, array[k]

    return array
