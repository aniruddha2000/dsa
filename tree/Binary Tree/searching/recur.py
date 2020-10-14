# Find the max element in the binary tree with recursion

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def search_ele(root, data):
    if root is not None:
        if data == root.val:
            return True
        else:
            temp = search_ele(root.left, data)
            if temp != 0:
                return temp
            else:
                return search_ele(root.right, data)
    else:
        return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(search_ele(root, 5))
