class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:
    def insert(self, root, key):
        # Simple insertion
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update the height after insertion
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # Check if tree is unbalanced
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Rotation
        y.left = z
        z.right = T2

        # Update height
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y  # new root

    def rightRotate(self, z):
        y = z.left
        T2 = y.right

        # Rotation
        y.right = z
        z.left = T2

        # Update height
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y  # new root

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

def preorder_trav(root):
    if root:
        print(root.val, end=" ")
        preorder_trav(root.left)
        preorder_trav(root.right)

my_tree = AVL_Tree()
root = None
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    root = my_tree.insert(root, key)

preorder_trav(root)
print()
