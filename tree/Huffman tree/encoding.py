from queue import Queue

class HuffmanNone:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None


def printCode(root, s):
    if root.left == None and root.right == None:
        print(root.data + ":" + s)
        return
    printCode(root.left, s+"0")
    printCode(root.right, s+"1")

def makeHuffmanNone(arr, freq, size):
    # freq = sorted(freq, reverse=True)
    q = Queue()
    for i in range(0, size):
        h_node = HuffmanNone(arr[i], freq[i])
        q.put(h_node)

    root = None
    while q.qsize() > 1:
        frst_min = q.get()
        scnd_min = q.get()

        non_leaf = HuffmanNone(None, (frst_min.freq+scnd_min.freq))
        non_leaf.left = frst_min
        non_leaf.right = scnd_min
        root = non_leaf
        q.put(non_leaf)
    printCode(root, "")



if __name__ == "__main__":
    arr = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [5, 9, 12, 13, 16, 45]
    size = len(arr)
    makeHuffmanNone(arr, freq, size)