# https://practice.geeksforgeeks.org/problems/maximum-collatz-sequence-length5849/1#

class Solution:
    def lengthN(self, n, cache):
        if n == 1:
            return {1: 1}
        temp = n
        count = 1
        while temp > 1:
            if temp % 2:
                temp = 3 * temp + 1
            else:
                temp /= 2
            if cache.get(temp) is not None:
                count = count + cache[temp]
                break
            count += 1
        cache[int(n)] = count
        return cache

    def collatzLength(self, N):
        cache = {}
        for i in range(1, N + 1):
            cache = self.lengthN(i, cache)
        return max(cache.values())


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.collatzLength(N))
