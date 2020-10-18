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

def inorder_trav(root):
    if root:
        inorder_trav(root.left)
        print(root.val, end=" ")
        inorder_trav(root.right)

def find_inorder_succ(root):
    while root.left:
        root = root.left
    return root

def delete_node(root, data):
    # if root == None:
    #     return "Empty tree"
    parent = None
    curr = root
    while curr and curr.val != data:
        parent = curr
        if data < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    if curr is None:
        return root

    # case 1(node has no child):
    if curr.left == None and curr.right == None:
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None

    # case 3(node has both child):
    elif curr.left and curr.right:
        inorder_succ = find_inorder_succ(curr.right)
        curr.val = inorder_succ.val
        delete_node(root, inorder_succ.val)

    # case 2(node has one child):
    else:
        if curr.left:
            child = curr.left
        else:
            child = curr.right

        if curr != root:
            if curr == parent.left:
                parent.left = child
                curr = None
                child = None
            else:
                parent.right = child
                curr = None
                child = None
        else:
            root = child
    return root


root = None
keys = [8, 10, 3, 1, 6, 5, 9, 14, 12, 17]

for key in keys:
    root = insert(root, key)
inorder_trav(root)
print()
root = delete_node(root, 10)
inorder_trav(root)
print()
