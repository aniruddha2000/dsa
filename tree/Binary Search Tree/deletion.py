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

def find_inorder_succ(root):
    while root.left is not None:
        root = root.left
    return root

def delete_node(root, data):
    if root == None:
        return "Empty tree"
    parent = None
    curr = root
    while curr and curr.val != data:
        parent = curr
        if data < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    # case 1(node has no child):
    if curr.left == None and curr.right == None:
        if parent.left == curr:
            parent.left = None
        else:
            parent.right = None

    # case 2(node has one child):
    elif curr.left != None or curr.right != None:
        if curr.left:
            child = curr.left
        else:
            child = curr.right

        if curr == parent.left:
            parent.left = child
            curr = None
            child = None
        else:
            parent.right = child
            curr = None
            child = None
    return root


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.right.left = Node(9)
root.right.right = Node(14)
root.right.right.right = Node(17)
inorder_trav(root)
print()
root = delete_node(root, 6)
inorder_trav(root)
