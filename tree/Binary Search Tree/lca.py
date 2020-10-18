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

def lca(root, n1, n2):
    while root:
        if root.val < n1 and root.val < n2:
            root = root.right
        elif root.val > n1 and root.val > n2:
            root = root.left
        else:
            break
    return root.val


root = None
keys = [8, 10, 3, 1, 6, 5, 9, 14, 12, 17]

for key in keys:
    root = insert(root, key)
node = lca(root, 5, 12)
print(node)
