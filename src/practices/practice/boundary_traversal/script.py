# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return a list containing the boundary view of the binary tree
class Solution:

    def printMidSubBoundary(self, node, arr):
        if node is None:
            return
        if node.left is None and node.right is None:
            arr.append(node.data)
        else:
            self.printMidSubBoundary(node.left, arr)
            self.printMidSubBoundary(node.right, arr)

    def printLeftSubBoundary(self, node, arr):
        if node is None:
            return
        arr.append(node.data)
        self.printLeftSubBoundary(node.left, arr)
        self.printMidSubBoundary(node.right, arr)

    def printRightSubBoundary(self, node, arr):
        if node is None:
            return
        self.printMidSubBoundary(node.left, arr)
        self.printRightSubBoundary(node.right, arr)
        arr.append(node.data)

    def printBoundaryView(self, root):
        arr = []
        arr.append(root.data)
        self.printLeftSubBoundary(root.left, arr)
        self.printRightSubBoundary(root.right, arr)
        return arr

# Code here

#{
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip=list(map(str,s.split()))

    # Create the root of the tree
    root=Node(int(ip[0]))
    size=0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size+1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1

        # Get the current node's value from the string
        currVal=ip[i]

        # If the left child is not null
        if(currVal!="N"):

            # Create the left child for the current node
            currNode.left=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        # If the right child is not null
        if(currVal!="N"):

            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')



# } Driver Code Ends