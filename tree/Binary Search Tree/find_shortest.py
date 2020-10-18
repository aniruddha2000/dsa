# If both keys are greater than the current node, we move to the right child of the current node.
# If both keys are smaller than current node, we move to left child of current node.
# If one keys is smaller and other key is greater, current node is
# Lowest Common Ancestor (LCA) of two nodes.
# We find distances of current node from two keys and return sum of the distances.

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
    return root

def find_shortest(root, n1, n2):
    d1 = d2 = 0
    curr1 = curr2 = lca(root, n1, n2)
    if n1 > n2:
        n1, n2 = n2, n1
    while curr1.val != n1:
        if n1 < curr1.val:
            curr1 = curr1.left
            d1 += 1
        else:
            curr1 = curr1.right
            d1 += 1
    while curr2.val != n2:
        if n2 < curr2.val:
            curr2 = curr2.left
            d2 += 1
        else:
            curr2 = curr2.right
            d2 += 1
    return d1 + d2


root = None
keys = [8, 10, 3, 1, 6, 5, 9, 14, 12, 17]

for key in keys:
    root = insert(root, key)
node = find_shortest(root, 3, 10)
print(node)
