# https://practice.geeksforgeeks.org/problems/min-cost-climbing-stairs/1#

# Approach is to memorize the min cost for last two steps and use it to compute next step
# update the min_costs and move to next

class Solution:
    def minCostClimbingStairs(self, cost, N):
        mc1 = 0
        mc2 = 0

        for i in range(N):
            min_cost = cost[i] + min(mc1, mc2)
            mc1, mc2 = mc2, min_cost

        return min(mc1,mc2)


if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N=int(input())
        cost=list(map(int,input().split()))

        ob = Solution()
        print(ob.minCostClimbingStairs(cost,N))