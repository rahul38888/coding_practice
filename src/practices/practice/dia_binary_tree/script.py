# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

class Solution:
    def calculate_dimensions(self, root):
        if not root:
            return 0, 0
        dia_r, longest_hand_r = self.calculate_dimensions(root.right)
        dia_l, longest_hand_l = self.calculate_dimensions(root.left)

        dia = max(dia_l, dia_r, longest_hand_r + longest_hand_l + 1)
        longest_hand = max(longest_hand_l, longest_hand_r) + 1

        return dia, longest_hand

    def diameter(self, root):
        dia, _ = self.calculate_dimensions(root)
        return dia


from collections import deque
import sys

sys.setrecursionlimit(50000)


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None

    ip = list(map(str, s.split()))

    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
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
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        k = Solution().diameter(root)
        print(k)
