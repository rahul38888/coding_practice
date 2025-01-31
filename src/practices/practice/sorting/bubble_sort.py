
def bubble_sort(array: list[int], decreasing = False):
    n = len(array)
    for j in range(n - 1, -1, -1):
        for i in range(0, j):
            if not decreasing and array[i] >= array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            elif decreasing and array[i] <= array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


if __name__ == '__main__':
    arr1 = [1, 4, 5, 9, 0, 3, 5, 7, 8]
    arr2 = arr1.copy()

    bubble_sort(arr1)
    bubble_sort(arr2, True)

    print(f"Increasing {arr1}")
    print(f"Decreasing {arr2}")
