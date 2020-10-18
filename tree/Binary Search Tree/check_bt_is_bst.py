class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def checkBST(root):
    if root is None:
        return False
    if root.left != None and root.left.val > root.val:
        return False
    if root.right != None and root.right.val < root.val:
        return False
    if checkBST(root.left) is None or checkBST(root.right) is None:
        return False
    return True

root = None
keys = [8, 10, 3, 1, 6, 5, 9, 14, 12, 17]

for key in keys:
    root = insert(root, key)

if checkBST(root):
    print("Is BST")
else:
    print("Not a BST")
