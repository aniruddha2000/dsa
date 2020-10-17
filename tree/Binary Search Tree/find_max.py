class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def find_max(root):
    if root == None:
        return "Empty tree"
    while root.right != None:
        root = root.right
    return root.val


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.left = Node(9)
root.right.right = Node(14)
print(find_max(root))
