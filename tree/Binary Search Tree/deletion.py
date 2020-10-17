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

def delete_node(root, data):
    if root == None:
        return "Empty tree"
    while root:
        if root.val == data:
            if root.left == None and root.left == None:
                root = None
                return "Deleted"
            elif root.left == None or root.right == None:
                if root.left != None:
                    child = root.left
                    root = child
                    child = None
                else:
                    child = root.right
                    root = child
                    child = None
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
root.left.right.left = Node(5)
root.right.left = Node(9)
root.right.right = Node(14)
print(delete_node(root, 6))
