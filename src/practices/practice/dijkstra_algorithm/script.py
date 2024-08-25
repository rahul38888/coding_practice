import math
from collections import deque
from typing import List

# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
#
# Observation:
#   - This problem can be solved using BFS as well as DFS graph traversal. as well need to calculate all vertex distance
#   - We are using BFS here
#   - We will keep a queue to keep vertex we encounter but will process it when they come out of the queue
#   - For each vertex we will compute the distance as (dist of last vertex + weight of the edge we used)
#   - If this distance is less than previously calculated distance, then
#       - update the distance for the vertex with the new distance
#       - At this point also add the vertex to the queue
#


class Solution:

    def dijkstra(self, vs: int, es: List[List[int]], s: int) -> List[int]:
        queue = deque([s])
        in_queue = [False for _ in range(vs)]
        in_queue[s] = True
        dist = [math.inf for _ in range(vs)]
        dist[s] = 0

        while len(queue):
            cur = queue.popleft()
            in_queue[cur] = False
            children = es[cur]
            for child, d in children:
                if dist[child] > dist[cur] + d:
                    dist[child] = dist[cur] + d
                    if not in_queue[child]:
                        queue.append(child)

        return dist


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()
