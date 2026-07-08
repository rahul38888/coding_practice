class Node:
    def __init__(self, value, top, right, left):
        self.value = value
        self.top = top
        self.right = right
        self.left = left

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{\"" + str(self.value) + "\": { \"l\": " + str(self.left) + ", \"r\": " + str(self.right) + "}}"


class BST:
    def __init__(self, n, a):
        self.size = n
        self.root = convert(n, a, None)

    def __str__(self):
        return str(n) + " : " + str(self.root)


def convert(n, a, top):
    if n < 1:
        return None;
    root = Node(a[0])
    root.top = top
    root.left = None
    root.right = None

    if n == 1:
        return root;

    l_end, l_start = -2, -1
    r_end, r_start = -2, -1
    for i in range(1, n):
        if a[i] < a[0]:
            if l_start is -1:
                l_start, l_end = i, i
            else:
                l_end = i
        elif a[i] > a[0]:
            if r_start is -1:
                r_start, r_end = i, i
            else:
                r_end = i

    root.left = convert(l_end - l_start + 1, a[l_start:l_end+1], root)
    root.right = convert(r_end - r_start + 1, a[r_start:r_end+1], root)

    return root


def inOrderTraversal(root, k):
    if k is 0 or root is None:
        return 0, 0
    sum = 0
    if root.left:
        sum_par, k = inOrderTraversal(root.left, k)
        sum += sum_par

    if k > 0:
        sum += root.value
        k -= 1

    if k > 0 and root.right:
        sum_par, k = inOrderTraversal(root.right, k)
        sum += sum_par

    return sum, k


def smallest_k_BST(n, a, k):
    bst = BST(n, a)
    root = bst.root;
    sum, r_k = inOrderTraversal(root, k);
    return sum


def scan_input():
    n = int(input())

    nsstr = input()
    bst = list(map(lambda x: int(x), nsstr.split()))

    k = int(input())

    return n, bst, k


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, bst, k = scan_input()
        print(smallest_k_BST(n, bst, k))
