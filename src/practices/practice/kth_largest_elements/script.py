import heapq

class Solution:
    """
        Problem: https://www.geeksforgeeks.org/batch/gts-1/track/GTS-ARRAY/problem/k-largest-elements4206

        Observations
        ------------
        Simplest solution can be to sort the array using a performant working algorithm and fetch the k largest elements

        Solution
        ---------
        Start adding each element to a min-heap. If heap size goes above k pop min element
            Exit when there is no element to put into arr left

        From heap pop all elements one by one into an array. Return that array in reverse order
    """

    def kLargest(self, arr, n, k):
        heap = []
        for a in arr:
            heapq.heappush(heap, a)
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while len(heap):
            result.append(heapq.heappop(heap))

        return result[::-1]


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1
