from heapq import heapify, heappop, heappush
import math


class MinHeap:
    def __init__(self):
        self.heap = []

    def setHeap(self,heap):
        self.heap = heap

    def getParent(self, i):
        return math.floor((i - 1) / 2)

    def getLeftChild(self, i):
        return 2*i+1

    def getRighChild(self, i):
        return 2*i+2

    def getMin(self):
        if len(self.heap) <= 0:
            return None
        return self.heap[0]

    def insertKey(self, k):
        heappush(self.heap, k)

    def decreaseKey(self, i, val):
        if len(self.heap) <= 0:
            return None
        self.heap[i] = val
        heapify(self.heap)

    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self, i):
        self.decreaseKey(i, -float('inf'))
        self.extractMin()


if __name__ == '__main__':
    a = [1, 3, 6, 5, 9, 8]
    min_heap = MinHeap()
    min_heap.setHeap(a)
    print(str(min_heap))

    min_heap.insertKey(2)
    print(str(min_heap))

    min_heap.decreaseKey(3, 0)
    print(str(min_heap))

    min_heap.extractMin()
    print(str(min_heap))

    min_heap.deleteKey(4)
    print(str(min_heap))