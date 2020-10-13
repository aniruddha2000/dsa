# Find the max element in the binary tree with recursion

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def find_max(root):
    if root is not None:
        maximim = root.val
        if root.left is not None:
            left = find_max(root.left)
            maximim = max(maximim, left)
        if root.right is not None:
            right = find_max(root.right)
            maximim = max(maximim, right)
    return maximim

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(find_max(root))
