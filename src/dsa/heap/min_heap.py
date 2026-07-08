import math


class MinHeap:

    def __init__(self):
        self.heap = []

    def setHeap(self, heap):
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

    def upHeap(self, i):
        if len(self.heap) <= 0:
            return
        while i != 0 and self.heap[self.getParent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.getParent(i)] = self.heap[self.getParent(i)], self.heap[i]
            i = self.getParent(i)

    def insertKey(self, k):
        self.heap.append(k)
        i = len(self.heap)-1
        self.upHeap(i)

    # new_val < self.heap[i]
    def deceaseKey(self, i, new_val):
        if len(self.heap) <= 0:
            return
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


if __name__ == '__main__':
    a = [1, 3, 6, 5, 9, 8]
    min_heap = MinHeap()
    min_heap.setHeap(a)
    print(str(min_heap))

    min_heap.insertKey(2)
    print(str(min_heap))

    min_heap.deceaseKey(3, 0)
    print(str(min_heap))

    min_heap.extractMin()
    print(str(min_heap))

    min_heap.deleteKey(4)
    print(str(min_heap))


