
class Solution:
    # def allPossibleNs(self, n, cache):
    #     arr = []
    #     if n == 1:
    #         cache[1] = [[1]]
    #     if cache.__contains__(n):
    #         return cache
    #     for i in range(1, n+1):
    #         if i == n:
    #             arr.append([n])
    #             continue
    #         if not cache.__contains__(n - i):
    #             cache = self.allPossibleNs(n-i, cache)
    #         for pos in cache[n-i]:
    #             temp = [i]
    #             temp.extend(pos)
    #             arr.append(temp)
    #
    #     cache[n] = arr
    #     return cache
    #
    # def mergeParans(self, a, b):
    #     if len(a) is 0:
    #         return b
    #     if len(b) is 0:
    #         return a
    #     result = []
    #     for o in a:
    #         result.extend(list(map(lambda x: o+x, b)))
    #     return result
    #
    # def allParenthesis(self, n, cache, cache2):
    #     if n is 1:
    #         cache[1] = ["()"]
    #         return cache, cache2
    #
    #     if not cache2.__contains__(n):
    #         cache2[n] = self.allPossibleNs(n,cache={})
    #     a = cache2[n]
    #     result = []
    #     for pos in a[n]:
    #         parans = []
    #         for i in pos:
    #             if i == n:
    #                 result.append("("*i + ")"*i)
    #                 continue
    #             if not cache.__contains__(i):
    #                 cache, cache2 = self.allParenthesis(i, cache, cache2)
    #             parans = self.mergeParans(parans, cache[i])
    #         result.extend(parans)
    #     cache[n] = list(set(result))
    #     return cache, cache2

    def allParenthesis(self, str, n, o, c, result):
        if c == n:
            result.append(str)
            return  result
        else:
            if o > c:
                result = self.allParenthesis(str+")",n,o,c+1,result)
            if o < n:
                result = self.allParenthesis(str+"(",n,o+1,c,result)
            return result


    def AllParenthesis(self, n):
        result = self.allParenthesis("", n, 0, 0, [])
        return result


if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result= ob
        result.sort()
        for i in range(0,len(result)):
            print(result[i])

