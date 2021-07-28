import math


class MaxHeap:
    def __init__(self):
        self.heap = []

    def setHeap(self, heap):
        self.heap = heap

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

    def __str__(self):
        return str(self.heap)


if __name__ == '__main__':
    a = [9, 8, 6, 5, 2, 1]
    max_heap = MaxHeap()
    max_heap.setHeap(a)
    print(str(max_heap))

    max_heap.insertKey(7)
    print(str(max_heap))

    max_heap.increaseKey(3, 10)
    print(str(max_heap))

    max_heap.extractMax()
    print(str(max_heap))

    max_heap.deleteKey(4)
    print(str(max_heap))
