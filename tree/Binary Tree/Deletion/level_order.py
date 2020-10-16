from queue import Queue


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def inorder(root):
    if(not root):
        return
    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)

def find_deepest(root):
    queue = Queue()
    queue.put(root)
    while queue.qsize() > 0:
        temp_node = queue.get()
        if temp_node.left is not None:
            queue.put(temp_node.left)
        if temp_node.right is not None:
            queue.put(temp_node.right)
    return temp_node

def delete_depest(root, deepest):
    queue = Queue()
    queue.put(root)
    while queue.qsize() > 0:
        temp_node = queue.get()
        if temp_node.val == deepest:
            temp_node = None
            return
        if temp_node.right is not None:
            if temp_node.right == deepest:
                temp_node.right = None
                return
            else:
                queue.put(temp_node.right)
        if temp_node.left is not None:
            if temp_node.left == deepest:
                temp_node.left = None
                return
            else:
                queue.put(temp_node.left)

def del_node(root, data):
    queue = Queue()
    queue.put(root)
    deepest = find_deepest(root)
    while queue.qsize() > 0:
        temp_node = queue.get()
        if data == temp_node.val:
            temp_node.val = deepest.val
            delete_depest(root, deepest)
            return root
        if temp_node.left is not None:
            queue.put(temp_node.left)
        if temp_node.right is not None:
            queue.put(temp_node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
inorder(root)
root = del_node(root, 4)
print()
inorder(root)
print()
