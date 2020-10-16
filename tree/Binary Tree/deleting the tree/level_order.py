from queue import Queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def del_node(root):
    queue = Queue()
    queue.put(root)
    while queue.qsize() > 0:
        temp_node = queue.get()
        if temp_node.left is not None:
            queue.put(temp_node.left)
        if temp_node.right is not None:
            queue.put(temp_node.right)
        temp_node = None
    root = None
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
del_node(root)
