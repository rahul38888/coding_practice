
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


def heapify(arr, n, pref):
    for i in range(n//2, -1, -1):
        arr = heapify_node(arr, i, n)

    return arr


class Solution:
    def relativeSort (self,A1, N, A2, M):
        pref = {}
        for a in A2:



if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))

        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")

        print ()

        t -= 1
