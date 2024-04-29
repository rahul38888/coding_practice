# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

class Solution:
    def traverse(self, V, adj, visited, v):
        visited[v] = True
        for i in adj[v]:
            if visited[i]:
                return 1, visited
            status, visited = self.traverse(V, adj, visited, i)
            if status:
                return 1, visited
        return 0, visited

    def isCyclic(self, V, adj):
        visited = [False for i in range(V)]
        for i in range(V):
            if len(adj[i]) > 0:
                status, visited = self.traverse(V, adj, visited, i)
                return status

import sys

sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)