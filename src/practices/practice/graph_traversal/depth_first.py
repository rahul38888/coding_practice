
class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = list()

    def add_neighbor(self, neighbor: "Node"):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f"N<{self.data}>"


def dfs_recursive_traversal(node: Node, visited=None):
    if visited is None:
        visited = set()

    print(f"At {node}")
    visited.add(node)
    for nei in node.neighbors:
        if nei not in visited:
            dfs_recursive_traversal(nei, visited)
        else:
            print(f"Loop at {nei}")


def dfs_iterative(node: Node, visited=None):
    if visited is None:
        visited = set()

    stack = [node]

    while len(stack) > 0:
        cur = stack.pop()
        print(f"At {cur}")
        visited.add(cur)
        for nei in cur.neighbors:
            if nei not in visited:
                stack.append(nei)
            else:
                print(f"Loop at {nei}")


from collections import deque


def bfs_traversal(node: Node, visited=None):
    if visited is None:
        visited = []

    queue = deque([node])
    while len(queue) > 0:
        cur = queue.popleft()
        print(f"At {cur}")
        visited.add(cur)
        for nei in cur.neighbors:
            if nei not in visited:
                queue.append(nei)
            else:
                print(f"Loop at {nei}")


def build_graph() -> list[Node]:
    # 1 ->2 ->3 ->4 ->5 ->6     9 ->10 ->11 -
    #     |   .   ^  ^   |               ^ _ |
    #     .   |    \ |   .
    #    13   12     8<- 7
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 5),
             (8, 4), (12, 3), (2, 13), (9, 10), (10, 11), (11, 11)]

    node_map = dict()
    for fr, to in edges:
        if fr not in node_map:
            node_map[fr] = Node(fr)
        fr_node = node_map[fr]

        if to not in node_map:
            node_map[to] = Node(to)
        to_node = node_map[to]

        fr_node.add_neighbor(to_node)

    return list(node_map.values())


if __name__ == '__main__':
    nodes = build_graph()

    vis = set()
    for n in nodes:
        if n not in vis:
            # dfs_recursive_traversal(n, vis)
            # dfs_iterative(n, vis)
            bfs_traversal(n, vis)

