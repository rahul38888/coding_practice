# https://www.geeksforgeeks.org/problems/longest-repeating-and-non-overlapping-substring3421/1
#
# We can solve this problem in O(n^3) by brute force
#
# Observations:
#   - If 2 substrings are starting at i and j and ending at x and y then following will be true
#       - Obviously i < x < j < y < n
#   - If we have longest substrings of length L ending at i and j,
#     then length of longest substring ending at i+1 and j+1 would be
#       - L + 1 if (i+1)th and (j+1)th characters are same
#       - else 0
#
# We can use the above 2 properties to solve above problem in O(n^2)
#


class Solution:
    def longestSubstring_n3(self, s, n):
        length = 0
        index = 0

        for i in range(n):
            for j in range(i + 1, n):
                if i >= j or s[i] != s[j]:
                    continue
                x, y = i, j
                while y < n and x < j:
                    if s[x] != s[y]:
                        break
                    if length < x - i + 1:
                        length = x - i + 1
                        index = i
                    x += 1
                    y += 1
        if length == 0:
            return -1
        return s[index:index + length]

    def longestSubstring(self, s, n):
        length = 0
        index = 0

        comp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(n):
            for j in range(i + 1, n):
                if i >= j or s[i] != s[j]:
                    continue
                if comp[i][j] < (j - i):
                    comp[i+1][j+1] = comp[i][j] + 1
                    if comp[i+1][j+1] > length:
                        length = comp[i+1][j+1]
                        index = max(i, index)

        if length == 0:
            return -1
        return s[index-length+1:index+1]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.longestSubstring(S, len(S)))
