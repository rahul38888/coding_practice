#User function Template for python3

# design the class in the most optimal way

# key, value, least used
#
# min_heap
# key -> min_heap
import math


class MinHeap:
    def __init__(self, cap):
        self.cap = cap
        self.heap = []

    def parent(self, i):
        return (i-1)//2

    def add(self, val):
        self.heap.append(val)
        i = len(self.heap)-1
        p = self.parent(i)
        while p>=0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i, p = p, self.parent(p)

    def get_min(self):
        return self.heap[0]

    def extract_min(self):
        val = self.get_min()
        self.heap[0] = math.inf
        # while


class LRUCache:

    #Constructor for initializing the cache capacity with the given value.
    def __init__(self,cap):
        self.cap = cap
        self.cache = {}

    #Function to return value corresponding to the key.
    def get(self, key):
        pass

    # Function for storing key-value pair.
    def set(self, key, value):
        pass
#code here



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list

        lru=LRUCache(cap)


        i=0
        q=1
        while q<=qry:
            qtyp=a[i]

            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends