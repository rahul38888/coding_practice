import math

class Solution:
    def longestSubsequence_n2(self, a, n):
        cache = [1]*n
        for i in range(1, n):
            for j in range(0, i):
                if a[j] < a[i] and cache[i] < cache[j] + 1:
                    cache[i] = cache[j] + 1
        return max(cache)

    def inBetweenPos(self, val, A, len):
        if val < A[0]:
            return -1
        elif val > A[len - 1]:
            return len
        r = len - 1
        l = 0
        while l+1 < r:
            m = math.floor((l+r)/2)
            if A[m] >= val:
                r = m
            else:
                l = m
        return r

    def longestSubsequence_nlogn(self, a, n):
        possibleSeq = [a[0]]
        len = 1
        for i in range(1,n):
            if possibleSeq[0] > a[i]:
                possibleSeq[0] = a[i]
            elif possibleSeq[len - 1] < a[i]:
                possibleSeq.append(a[i])
                len += 1
            else:
                possibleSeq[self.inBetweenPos(a[i], possibleSeq, len)] = a[i]
        return len


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.longestSubsequence_nlogn(a, n))


# if __name__ == '__main__':
#     ob = Solution()
#     print(str(ob.inBetweenPos(100, [0,1,4,5,6,8,10], 7)))