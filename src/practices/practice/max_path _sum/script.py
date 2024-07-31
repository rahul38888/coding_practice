# https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1

# Approach is to iterate over each 0th row element and try to find the max path from there
# for any index save the longest cost path from there and reuse it

class Solution:
    def recMaximumPath(self, N, m, index, cache):
        if index[0] == N-1:
            if cache[index[0]][index[1]] is None:
                cache[index[0]][index[1]] = m[index[0]][index[1]]
            return cache[index[0]][index[1]]

        if cache[index[0]][index[1]] is not None:
            return cache[index[0]][index[1]]

        max_cost = 0
        r = index[0]
        c = index[1]

        max_cost = max(max_cost,self.recMaximumPath(N, m, (r+1, c), cache))
        if c-1 >= 0:
            max_cost = max(max_cost,self.recMaximumPath(N, m, (r+1, c-1), cache))
        if c+1 < N:
            max_cost = max(max_cost,self.recMaximumPath(N, m, (r+1, c+1), cache))

        cache[index[0]][index[1]] = max_cost + m[index[0]][index[1]]
        return cache[index[0]][index[1]]

    def maximumPath(self, N, Matrix):
        cache = [[None for i in range(N)] for i in range(N)]
        max_cost = 0
        for i in range(N):
            max_cost = max(max_cost,self.recMaximumPath(N, Matrix,(0,i),cache))

        return max_cost


if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])

        ob = Solution()
        print(ob.maximumPath(N, Matrix))