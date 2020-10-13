class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def preorder_trav(root):
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        print(curr.val, end=" ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)


def inorder_trav(root):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if len(stack) == 0:
            break
        root = stack.pop()
        print(root.val, end=" ")
        root = root.right

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def postorder_trav(root):
    stack = []
    while True:
        while root:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        if len(stack) == 0:
            break
        root = stack.pop()
        if (root.right is not None and peek(stack) == root.right):
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            print(root.val, end=" ")
            root = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
# preorder_trav(root)
postorder_trav(root)
print()
