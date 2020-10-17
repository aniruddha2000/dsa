class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def inorder_trav(root):
    if root:
        inorder_trav(root.left)
        print(root.val, end=" ")
        inorder_trav(root.right)

def inserting_node(root, data):
    new_node = Node(data)
    if root == None:
        return "Empty tree"
    while root:
        parent = root
        if data < root.val:
            root = root.left
        else:
            root = root.right
    if data < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node
    return root


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.left = Node(9)
root.right.right = Node(14)
inserting_node(root, 5)
inserting_node(root, 17)
inorder_trav(root)
