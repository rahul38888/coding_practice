

def heapify_node(arr, i, n):
    l = 2*i + 1
    r = 2*i + 2

    smallest = i
    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        arr = heapify_node(arr, smallest, n)

    return arr


def extract(arr,n):
    if n<1:
        return None
    val = arr[0]
    arr[0] = arr[n-1]
    if n-1 > 0:
        arr = heapify_node(arr, 0, n-1)
    return val, arr, n-1


def heapify(arr, n):
    for i in range(n//2, -1, -1):
        arr = heapify_node(arr, i, n)

    return arr


def heap_sort(array, length):
    array = heapify(array, length)

    result = []
    while length > 0:
        val, arr, length = extract(array, length)
        result.append(val)

    return result