class Solution:
    '''
        Problem: https://www.geeksforgeeks.org/batch/gts-1/track/GTS-ARRAY/problem/k-largest-elements4206

        Observations
        ------------
        Simplest sollution can be to sort the array ysing a performant sorking algorithm and fetch k element largest ones.

        Another sollution could be to start sorting the array with binary sort algorithm in decreasing order and stop when sorted part is of size we need.
        This way we need not ro sort whole array, kust k largest.

        Solution:
            - Start sorting using  binary sort algorithm in decreasing order.
            - Keep track of the size of sorted array. If it is equla to k, return the sorted subarray.
    '''
    def kLargest(self,arr, n, k):
	    pass


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