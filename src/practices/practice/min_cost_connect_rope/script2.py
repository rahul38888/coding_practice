import math
import heapq


class MinHeap:
    def __init__(self, heap):
        self.heap = heap

    def setHeap(self, heap):
        self.heap = heap

    def getParent(self, i):
        return math.floor((i - 1) / 2)

    def getLeftChild(self, i):
        return 2 * i + 1

    def getRighChild(self, i):
        return 2 * i + 2

    def getMin(self):
        if len(self.heap) <= 0:
            return None
        return self.heap[0]

    def upHeap(self, i):
        if len(self.heap) <= 0:
            return
        while i is not 0 and self.heap[self.getParent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.getParent(i)] = self.heap[self.getParent(i)], self.heap[i]
            i = self.getParent(i)

    def insertKey(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        self.upHeap(i)

    def deceaseKey(self, i, new_val):
        if len(self.heap) <= 0:
            return None
        self.heap[i] = new_val
        self.upHeap(i)

    def downHeap(self, i):
        length = len(self.heap)

        while True:
            l, r = self.getLeftChild(i), self.getRighChild(i)
            smallest = i
            if l < length and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < length and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest is not i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def extractMin(self):
        if len(self.heap) <= 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop(0)

        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.downHeap(0)

        return result

    def deleteKey(self, i):
        self.deceaseKey(i, -float('inf'))
        self.extractMin()

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)


def merge(arr, s, m, e):
    i = s
    j = m + 1
    sorted_sub_arr = []
    while i <= m and j <= e:
        if arr[i] <= arr[j]:
            sorted_sub_arr.append(arr[i])
            i += 1
        else:
            sorted_sub_arr.append(arr[j])
            j += 1
    while i <= m:
        sorted_sub_arr.append(arr[i])
        i += 1
    while j <= e:
        sorted_sub_arr.append(arr[j])
        j += 1

    arr[s:e + 1] = sorted_sub_arr
    return arr


def sort(arr, s, e):
    if s >= e:
        return arr
    m = int((s + e) / 2)
    arr = sort(arr, s, m)
    arr = sort(arr, m + 1, e)
    arr = merge(arr, s, m, e)
    return arr


class Solution:
    def minCost(self, arr, n):
        arr = sort(arr, 0, n - 1)
        print(arr)
        heap = MinHeap(arr)
        result = 0
        while len(heap) > 1:
            min1 = heap.extractMin()
            min2 = heap.getMin()
            new_rope = min1+min2
            heap.heap[0] = new_rope
            heap.downHeap(0)
            result += new_rope

        return result

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a, n))
