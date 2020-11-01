from queue import Queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def find_height(root):
    if root is None:
        return -1
    queue = Queue()
    queue.put(root)
    height = 0
    while True:
        node_count = queue.qsize()
        if node_count == 0:
            return height
        height += 1

        while node_count > 0:
            temp_node = queue.get()
            if temp_node.left is not None:
                queue.put(temp_node.left)
            if temp_node.right is not None:
                queue.put(temp_node.right)
            node_count -= 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(find_height(root))
