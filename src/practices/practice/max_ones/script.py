
class Solution:
    def rowWithMax1s(self,arr, n, m):
        index = -1

        j = m - 1
        for i in range(n):
            while j >= 0:
                if arr[i][j] is 1:
                    index = i
                else:
                    break
                j -= 1

        return index


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1
