
class Solution:
    def build(self, inorder, preorder):
        if len(inorder) is 0:
            return None, preorder
        root = Node(preorder[0])
        splti = inorder.index(root.data)
        preorder = preorder[1:]
        if splti is 0:
            return root, preorder
        root.left, preorder = self.build(inorder[:splti], preorder)
        root.right, preorder = self.build(inorder[splti+1:], preorder)

        return root, preorder

    def buildtree(self, inorder, preorder, n):
        root, p = self.build(inorder, preorder)
        return root


class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]

        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()
