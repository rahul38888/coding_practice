# https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1#

# Approach is to keep the state of visited nodes by assigning data = None
# iterate over the linked list until there are no nodes,
# check if data is None
#   if None then it has been visited, return True
#   else at the end of the iteration return False

# Floyd’s Cycle-Finding Algorithm can be used in place of this
class Solution:
    def detectLoopFlagedBased(self, head):
        cur = head
        while cur is not None:
            if cur.data is None:
                return True
            cur.data = None
            cur = cur.next
        return False

    def detectLoop(self, head):
        S, F = head, head
        while F is not None:
            S = S.next
            if F.next is None:
                return False
            else:
                F = F.next.next

            if S is F:
                return True
        return False


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))

        print(Solution().detectLoop(LL.head))
