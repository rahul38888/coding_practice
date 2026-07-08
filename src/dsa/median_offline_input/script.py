import math


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


def get_new_median(val, m, lheap, rheap):
    new_m = 0
    if len(lheap) == len(rheap):
        if val < m:
            lheap.insertKey(val)
            new_m = lheap.getMax()
        else:
            rheap.insertKey(val)
            new_m = rheap.getMin()
    elif len(lheap) < len(rheap):
        if val < m:
            lheap.insertKey(val)
        else:
            lheap.insertKey(rheap.extractMin())
            rheap.insertKey(val)
        new_m = (rheap.getMin() + lheap.getMax()) / 2
    else:
        if val < m:
            rheap.insertKey(lheap.extractMax())
            rheap.insertKey(val)
        else:
            rheap.insertKey(val)
        new_m = (rheap.getMin() + lheap.getMax()) / 2

    return new_m


def offline_median(a, n):
    lheap = MaxHeap()
    rheap = MinHeap()

    m = - float('inf')
    for val in a:
        m = get_new_median(val, m, lheap, rheap)
        print(m)


def scan_input():
    n = int(input())
    nsstr = input()
    a = list(map(lambda x: int(x), nsstr.split()))
    return a, n


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        a, n = scan_input()
        offline_median(a, n)
