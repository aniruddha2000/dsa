from collections import OrderedDict


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printTopViewUtil(root, height, level, m):
    if root is None:
        return
    if level not in m:
        m[level] = [root.data, height]
    else:
        p = m[level]
        if p[1] > height:
            m[level] = [root.data, height]

    printTopViewUtil(root.left, height+1, level-1, m)
    printTopViewUtil(root.right, height+1, level+1, m)


def printTopView(root):
    m = OrderedDict()
    printTopViewUtil(root, 0, 0, m)
    for i in sorted(list(m)):
        p = m[i]
        print(p[0], end=" ")


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)

print("Top View : ", end="")
printTopView(root)
print()
