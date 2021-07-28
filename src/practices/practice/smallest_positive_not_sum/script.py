from math import floor


class Solution:
    def smallestpositive(self, array, n):
        array.sort()
        cur = array[0]
        if cur is not 1:
            return 1
        for i in range(1,n):
            val = array[i]
            if val <= cur+1:
                cur = max(cur, val+cur)
            else:
                break
        return cur+1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array,n))