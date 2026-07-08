

def partition(array: list[int], s: int, e: int, decreasing=False) -> int:
    pivot = array[e]
    i = s - 1

    for j in range(s, e):
        if not decreasing and array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        elif decreasing and array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[e], array[i + 1] = array[i + 1], array[e]
    return i + 1


def quick_sort_internal(array: list[int], s: int, e: int, decreasing=False):
    if s < e:
        pivot_index = partition(array, s, e, decreasing)
        quick_sort_internal(array, s, pivot_index - 1, decreasing)
        quick_sort_internal(array, pivot_index + 1, e, decreasing)


def quick_sort(array: list[int], decreasing=False):
    quick_sort_internal(array, 0, len(array) - 1, decreasing)


if __name__ == '__main__':
    arr1 = [1, 4, 5, 9, 0, 3, 5, 7, 8]
    arr2 = arr1.copy()

    quick_sort(arr1)
    quick_sort(arr2, True)

    print(f"Increasing {arr1}")
    print(f"Decreasing {arr2}")