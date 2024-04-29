# https://practice.geeksforgeeks.org/problems/sum-of-query-ii5310/1#

# Approach is to keep an array of size n+1 with 0th element = 0 and
# ith element sum of all elements from 0 to i-1 in arr

# to get sum from l to r, just use sums[r] - sums[l-1]

class Solution:
    def querySum(self, n, arr, q, queries):
        sums = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + arr[i - 1]

        result = []
        for i in range(q):
            l = queries[2 * i]
            r = queries[2 * i + 1]
            result.append(sums[r] - sums[l - 1])

        return result


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        q = int(input())
        queries = input().split()
        for i in range(0, 2 * q, 2):
            queries[i] = int(queries[i])
            queries[i + 1] = int(queries[i + 1])

        ob = Solution()
        ans = ob.querySum(n, arr, q, queries)
        for it in ans:
            print(it, end=" ")
        print()
