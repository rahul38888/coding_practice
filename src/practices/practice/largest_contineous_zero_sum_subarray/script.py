# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#

# Approach is to iterate over list and and store sum and index in hashed map if not present
# if sum already present update max_len with (cur index - index present for the sum in map)

class Solution:
    def maxLen(self, n, arr):
        sum_hashed = dict()
        sum_hashed[0] = -1
        s = 0
        max_len = 0
        for i in range(n):
            s += arr[i]
            if sum_hashed.__contains__(s):
                max_len = max(max_len, i - sum_hashed[s])
            else:
                sum_hashed[s] = i

        return max_len


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n, arr))
