# User function Template for python3

class MaxHeap:
    def __init__(self):
        self.heap = []

    def getParent(self, i):
        return math.floor((i - 1) / 2)

    def getLeftChild(self, i):
        return 2 * i + 1

    def getRighChild(self, i):
        return 2 * i + 2

    def getMax(self):
        if len(self.heap) <= 0:
            return None
        return self.heap[0]

    def upHeap(self, i):
        if len(self.heap) <= 0:
            return
        while i is not 0 and self.heap[self.getParent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.getParent(i)] = self.heap[self.getParent(i)], self.heap[i]
            i = self.getParent(i)

    def insertKey(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        self.upHeap(i)

    # new_val > self.heap[i]
    def increaseKey(self, i, new_val):
        if len(self.heap) <= 0:
            return None
        self.heap[i] = new_val
        self.upHeap(i)

    def downHeap(self, i):
        length = len(self.heap)

        while True:
            l, r = self.getLeftChild(i), self.getRighChild(i)
            largest = i
            if l < length and self.heap[l] > self.heap[largest]:
                largest = l
            if r < length and self.heap[r] > self.heap[largest]:
                largest = r
            if largest is not i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def extractMax(self):
        if len(self.heap) <= 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop(0)

        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.downHeap(0)

        return result

    def deleteKey(self, i):
        self.increaseKey(i, float('inf'))
        self.extractMax()

    def __len__(self):
        return len(self.heap)


class MinHeap:

    def __init__(self):
        self.heap = []

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

    # new_val < self.heap[i]
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

    def __len__(self):
        return len(self.heap)


class Solution:

    def __init__(self):
        self.lheap = MaxHeap()
        self.rheap = MinHeap()

    def balanceHeaps(self):
        pass

    def getMedian(self):
        if len(self.lheap) == len(self.rheap):
            if len(self.rheap) == 0:
                return -float('inf')

            return (self.rheap.getMin() + self.lheap.getMax()) / 2
        elif len(self.lheap) < len(self.rheap):
            return self.rheap.getMin()
        else:
            return self.lheap.getMax()

    def insertHeaps(self, x):
        m = self.getMedian()
        if len(self.lheap) == len(self.rheap):
            if x < m:
                self.lheap.insertKey(x)
            else:
                self.rheap.insertKey(x)
        elif len(self.lheap) < len(self.rheap):
            if x < m:
                self.lheap.insertKey(x)
            else:
                self.lheap.insertKey(self.rheap.extractMin())
                self.rheap.insertKey(x)
        else:
            if x < m:
                self.rheap.insertKey(self.lheap.extractMax())
                self.lheap.insertKey(x)
            else:
                self.rheap.insertKey(x)


import math

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        ob = Solution()
        for i in range(n):
            x = int(input())
            ob.insertHeaps(x)
            ob.balanceHeaps()
            print(math.floor(ob.getMedian()))
