# https://practice.geeksforgeeks.org/problems/maximum-path-sum/1
import math
from collections import deque
import sys


def maxSubTreeSum(root):
    if not root:
        return 0, 0

    max_sum_l, max_hand_sum_l = maxSubTreeSum(root.left)
    max_sum_r, max_hand_sum_r = maxSubTreeSum(root.right)

    max_sum = max(max_sum_l, max_sum_r, max_hand_sum_r + max_hand_sum_l + root.data)
    if not root.right or not root.left:
        max_sum = -math.inf
    max_hand_sum = max(max_hand_sum_l + root.data, max_hand_sum_r + root.data)

    return max_sum, max_hand_sum


def maxPathSum(root):
    max_sum, max_hand_sum = maxSubTreeSum(root)
    return max_sum


sys.setrecursionlimit(10 ** 6)


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
        print(maxPathSum(root))
