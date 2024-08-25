from collections import deque

# https://www.geeksforgeeks.org/problems/level-order-traversal/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
#
# Observation:
#   - We can use queue to keep order of access to tree nodes
#   - In this method at any node its children will be inserted into the queue and then new node will be accessed
#       which is on top of the queue


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def levelOrder(self, rn: Node) -> list:
        result = []
        if rn is None:
            return result

        queue = deque([rn])
        while len(queue):
            cur = queue.popleft()
            result.append(cur.data)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

        return result


def buildTree(string: str):
    if len(string) == 0 or string[0] == "N":
        return None

    ip = list(map(str, string.split()))

    root_node = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root_node)
    size = size + 1

    i = 1
    while size > 0 and i < len(ip):
        currNode = q[0]
        q.popleft()
        size = size - 1

        currVal = ip[i]

        if currVal != "N":
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size = size + 1
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        if currVal != "N":
            currNode.right = Node(int(currVal))

            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root_node


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        res = Solution().levelOrder(root)
        for i in res:
            print(i, end=" ")
        print()