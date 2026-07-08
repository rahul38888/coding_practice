# https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1#

# The approach is to keep a level accumulator which keep adding entries for a level
# Use a queue to keep the nodes to process and loop until it is empty
# to process a node add it in accumulator and add left and then left in the queue

from queue import Queue


class Solution:
    def verticalOrder(self, root):
        v_levels = {}
        q = Queue()
        q.put((root, 0))
        min_level = 0
        max_level = 0
        while q.qsize():
            entry = q.get()
            level = entry[1]
            node = entry[0]
            if not v_levels.__contains__(level):
                v_levels[level] = []
            v_levels[level].append(node.data)

            if node.left is not None:
                q.put((node.left, level - 1))
                min_level = min(min_level, level - 1)
            if node.right is not None:
                q.put((node.right, level + 1))
                max_level = max(max_level, level + 1)

        result = []
        for level in range(min_level, max_level + 1):
            result += v_levels[level]

        return result


from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    import sys

    sys.setrecursionlimit(10000)
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        res = Solution().verticalOrder(root)
        for i in res:
            print(i, end=" ")
        print()
