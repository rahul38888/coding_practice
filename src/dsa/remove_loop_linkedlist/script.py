# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1#

# Approach is to use Floy'd loop finding algorithm
#   before meeting on starting point, remove the next pointer of loop
#   handle edge case when starting point is head by keeping s_prev

class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        if head is None:
            return

        s = head
        f = head
        s_prev = None
        while True:
            s_prev = s
            s = s.next
            f = None if f.next is None else f.next.next
            if f is None:
                return

            if s == f:
                break

        if s == head:
            s_prev.next = None
            return

        h = head
        while True:
            if s.next == h.next:
                s.next = None
                break

            h = h.next
            s = s.next


class Node:
    def __init__(self, val):
        self.next = None
        self.data = val


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, num):
        if self.head is None:
            self.head = Node(num)
            self.tail = self.head
        else:
            self.tail.next = Node(num)
            self.tail = self.tail.next

    def isLoop(self):
        if self.head is None:
            return False

        fast = self.head.next
        slow = self.head

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

    def loopHere(self, position):
        if position == 0:
            return

        walk = self.head
        for _ in range(1, position):
            walk = walk.next
        self.tail.next = walk

    def length(self):
        walk = self.head
        ret = 0
        while walk:
            ret += 1
            walk = walk.next
        return ret


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = tuple(int(x) for x in input().split())
        pos = int(input())

        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)

        Solution().removeLoop(ll.head)

        if ll.isLoop() or ll.length() != n:
            print(0)
            continue
        else:
            print(1)
