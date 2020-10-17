class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def searching_node(root, data):
    if root == None:
        return "Empty tree"
    while root:
        if root.val == data:
            return root.val
        elif data < root.val:
            root = root.left
        else:
            root = root.right
    return "Not found"


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.left = Node(9)
root.right.right = Node(14)
print(searching_node(root, 6))
