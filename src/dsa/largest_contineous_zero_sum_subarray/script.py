# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#
#
# Observations:
#   - Let a subarray with sum zero is [x ... y]
#       - If sum of subarray [0 ... x) is A then sum of subarray [0, y] is also A
#   - This is something we can use
#   - Start adding element in array one by one
#   - If at any point the current sum has seen observed previously, then
#       the subarray (previous sum index, current sum index] will be a 0 sum subarray
#   - Find all such subarray and return max size
#

class Solution:
    def maxLen(self, n_value: int, array: list):
        sum_hashed = dict()
        sum_hashed[0] = -1
        s = 0
        max_len = 0
        for j in range(n_value):
            s += array[j]
            if sum_hashed.__contains__(s):
                max_len = max(max_len, j - sum_hashed[s])
            else:
                sum_hashed[s] = j

        return max_len


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n, arr))
