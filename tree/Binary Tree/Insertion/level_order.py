from queue import Queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def insert_ele(root, data):
    new_node = Node(data)
    queue = Queue()
    queue.put(root)
    while queue.qsize() > 0:
        temp_node = queue.get()
        if temp_node.left is not None:
            queue.put(temp_node.left)
        else:
            temp_node.left = new_node
            break
        if temp_node.right is not None:
            queue.put(temp_node.right)
        else:
            temp_node.right = new_node
            break

def trav_tree(root):
    queue = Queue()
    queue.put(root)
    while queue.qsize() > 0:
        temp_node = queue.get()
        print(temp_node.val, end=" ")
        if temp_node.left is not None:
            queue.put(temp_node.left)
        if temp_node.right is not None:
            queue.put(temp_node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
trav_tree(root)
print()
insert_ele(root, 9)
trav_tree(root)
print()
print(root.left.left.right.val)
