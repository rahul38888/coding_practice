# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    def is_leaf(self):
        return not(self.right or self.left)

    def __str__(self) -> str:
        return str(self.data)

class Solution:

    def printLeftPart(self, node: Node, arr: list):
        if node:
            if node.left:
                arr.append(node.data)
                self.printLeftPart(node.left, arr)
            elif node.right:
                arr.append(node.data)
                self.printLeftPart(node.right, arr)

    
    def printRightPart(self, node: Node, arr: list):
        if node:
            if node.right:
                self.printRightPart(node.right, arr)
                arr.append(node.data)
            elif node.left:
                self.printRightPart(node.left, arr)
                arr.append(node.data)
    
    def printLeafPart(self, node: Node, arr: list):
        if node:
            if node.is_leaf():
                arr.append(node.data)
                return

            self.printLeafPart(node.left, arr)
            self.printLeafPart(node.right, arr)
        

    def printBoundaryView(self, root: Node):
        arr = []
        arr.append(root.data)
        self.printLeftPart(root.left, arr)
        self.printLeafPart(root.left, arr)
        self.printLeafPart(root.right, arr)
        self.printRightPart(root.right, arr)
        
        return arr
    

import sys

import sys
sys.setrecursionlimit(100000)
from collections import deque
# Tree Node

def buildTree(s):
    if(len(s)==0 or s[0]=="N"):
        return None

    ip=list(map(str,s.split()))

    root=Node(int(ip[0]))
    size=0
    q=deque()

    q.append(root)
    size=size+1

    i=1
    while(size>0 and i<len(ip)):
        currNode=q[0]
        q.popleft()
        size=size-1

        currVal=ip[i]

        if(currVal!="N"):

            currNode.left=Node(int(currVal))

            q.append(currNode.left)
            size=size+1
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        if(currVal!="N"):

            currNode.right=Node(int(currVal))

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
