# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

class Solution:
    def dfs_loop(self, v: int, adj: list, visited: list, path_stack: dict) -> bool:
        path_stack[v] = True
        visited[v] = True
        for v2 in adj[v]:
            if not visited[v2]:
                if self.dfs_loop(v2, adj, visited, path_stack):
                    return True
            
            elif path_stack.__contains__(v2) and path_stack[v2]:
                return True
            
        del path_stack[v]
        return False


    def isCyclic(self, V: int, adj: dict):
        visited = [False for i in range(V)]
        for v in range(V):
            if visited[v]:
                continue
            
            if self.dfs_loop(v, adj, visited, dict()):
                return True
        
        return False
            
            
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        _ = input()
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