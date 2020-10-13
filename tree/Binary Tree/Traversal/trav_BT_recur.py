class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def preorder_trav(root):
    if root:
        print(root.val, end=" ")
        preorder_trav(root.left)
        preorder_trav(root.right)

def inorder_trav(root):
    if root:
        inorder_trav(root.left)
        print(root.val, end=" ")
        inorder_trav(root.right)

def postorder_trav(root):
    if root:
        postorder_trav(root.left)
        postorder_trav(root.right)
        print(root.val, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("Preorder - ")
preorder_trav(root)
print()
print("Inorder - ")
inorder_trav(root)
print()
print("Postorder - ")
postorder_trav(root)
print()
