from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<{self.data}>"


def print_with_space(node: Node):
    print(node.data, end=" ")


class BinarySearchTree:
    def __init__(self, head):
        self.head = head

    def __in_order(self, node: Node, operation):
        if node:
            self.__in_order(node.left, operation)
            operation(node)
            self.__in_order(node.right, operation)

    def in_order(self, operation=None):
        if operation is None:
            operation = print_with_space

        self.__in_order(self.head, operation)

    def __post_order(self, node: Node, operation):
        if node:
            self.__post_order(node.left, operation)
            self.__post_order(node.right, operation)
            operation(node)

    def post_order(self, operation=None):
        if operation is None:
            operation = print_with_space

        self.__post_order(self.head, operation)

    def __pre_order(self, node: Node, operation):
        if node:
            operation(node)
            self.__pre_order(node.left, operation)
            self.__pre_order(node.right, operation)

    def pre_order(self, operation=None):
        if operation is None:
            operation = print_with_space

        self.__pre_order(self.head, operation)

    def level_order(self, operation=None):
        if self.head is None:
            return

        if operation is None:
            operation = print_with_space

        queue = deque([self.head])
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node is None:
                    continue
                operation(node)
                queue.append(node.left)
                queue.append(node.right)


def get_bst():
    #            1
    #     2             3
    # 4       5              6
    #       7   8
    head = Node(1)
    head.right = Node(3)
    head.right.right = Node(6)

    left = Node(2)
    left.left = Node(4)
    left.right = Node(5)
    left.right.left = Node(7)
    left.right.right = Node(8)

    head.left = left

    return head


if __name__ == '__main__':
    bst = BinarySearchTree(get_bst())

    result = []
    print("In Order")
    bst.in_order(result.append)
    print(result)

    result = []
    print("Post Order")
    bst.post_order(result.append)
    print(result)

    result = []
    print("Pre Order")
    bst.pre_order(result.append)
    print(result)

    result = []
    print("Level Order")
    bst.level_order(result.append)
    print(result)
