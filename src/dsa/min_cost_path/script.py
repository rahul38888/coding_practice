import math

class Solution:

    #Function to return the minimum cost to react at bottom
    #right cell from top left cell.

    # 	at every point calculate the minimum path to end recursivly
    def minFromNode(self, grid, i, j, passed, costs):
        if i == len(grid)-1 and j == len(grid)-1:
            print(passed)
            costs[i][j] = grid[i][j]
            return

        passed[i][j] = True
        min_cost = math.inf
        if i-1 >= 0:
            if costs[i-1][j] == None and not passed[i-1][j]:
                self.minFromNode(grid, i-1,j, passed, costs)
            min_cost = min(min_cost, grid[i][j] + costs[i-1][j])

        if j-1 >= 0:
            if costs[i][j-1] == None and not passed[i][j-1]:
                self.minFromNode(grid, i,j-1, passed, costs)
            min_cost = min(min_cost, grid[i][j] + costs[i][j-1])

        if i+1 < len(grid):
            if costs[i+1][j] == None and not passed[i+1][j]:
                self.minFromNode(grid, i+1,j, passed, costs)
            min_cost = min(min_cost, grid[i][j] + costs[i+1][j])

        if j+1 < len(grid):
            if costs[i][j+1] == None and not passed[i][j+1]:
                self.minFromNode(grid, i,j+1, passed, costs)
            min_cost = min(min_cost, grid[i][j] + costs[i][j+1])

        costs[i][j] = min_cost
        passed[i][j] = False

    def minimumCostPath(self, grid):
        passed = [[False for i in range(len(grid))] for j in range(len(grid))]
        costs = [[None for i in range(len(grid))] for j in range(len(grid))]
        self.minFromNode(grid, 0, 0, passed, costs)
        print(costs)
        return costs[0][0]


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.minimumCostPath(grid)
        print(ans)
