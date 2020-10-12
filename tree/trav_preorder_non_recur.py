class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def preorder_trav(root):
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        print(curr.val, end=" ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
preorder_trav(root)
