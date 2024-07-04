# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None

    def __str__(self):
        str = ""
        while self is not None:
            str += self.data + "- "
        node = self.bottom
        return str

def findMinimum(root: Node):
    min_prev, min = None, root
    cur_prev, cur = None, root
    while cur is not None:
        if cur.data < min.data:
            min_prev, min = cur_prev, cur
        cur_prev, cur = cur, cur.next

    return min, min_prev


def flatten(root):
    result = None
    result_cur = None
    while root is not None:
        min, min_prev = findMinimum(root)
        if result is None:
            result = Node(min.data)
            result_cur = result
        else:
            result_cur.bottom = Node(min.data)
            result_cur = result_cur.bottom

        if min_prev is None:
            if min.bottom is not None:
                min.bottom.next = min.next
                root = min.bottom
            else:
                root = min.next
        elif min.bottom is not None:
            min_prev.next, min.bottom.next = min.bottom, min.next
        elif min.next is not None:
            min_prev.next = min.next
        else:
            min_prev.next = None

    return result


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        head = None
        N = int(input())
        arr = []

        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag is 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 is 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        root = flatten(head)
        printList(root)

        t -= 1
