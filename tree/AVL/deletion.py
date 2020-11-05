class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:
    def insert(self, root, key):
        # Simple insertion
        if root is None:
            return Node(key)
        elif key < root.val:
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

    def deletion(self, root, key):
        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key < root.val:
            root.left = self.deletion(root.left, key)

        elif key > root.val:
            root.right = self.deletion(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.deletion(root.right,
                                     temp.val)

        if root is None:
            return root

        # AVL balancing
        # Update the height after deletion
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # Check if tree is unbalanced
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
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

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)


def preorder_trav(root):
    if root:
        print(root.val, end=" ")
        preorder_trav(root.left)
        preorder_trav(root.right)


my_tree = AVL_Tree()
root = None
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for key in keys:
    root = my_tree.insert(root, key)

preorder_trav(root)
print()

my_tree.deletion(root, 10)
preorder_trav(root)
print()
