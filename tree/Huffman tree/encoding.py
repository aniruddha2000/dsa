import heapq


class HuffmanNone:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HuffmanNone)):
            return False
        return self.freq == other.freq


def printCode(root, s):
    if root.left == None and root.right == None:
        print(root.data + ":" + s)
        return
    printCode(root.left, s+"0")
    printCode(root.right, s+"1")

def makeHuffmanNone(data, size):
    q = []
    for i in range(0, size):
        (char, freq) = data[i]
        h_node = HuffmanNone(char, freq)
        heapq.heappush(q, h_node)

    root = None
    while len(q) > 1:
        frst_min = heapq.heappop(q)
        scnd_min = heapq.heappop(q)

        non_leaf = HuffmanNone(None, (frst_min.freq+scnd_min.freq))
        non_leaf.left = frst_min
        non_leaf.right = scnd_min
        root = non_leaf
        heapq.heappush(q, non_leaf)
    printCode(root, "")



if __name__ == "__main__":
    string = "BCAADDDCCACACAC"
    data = {}
    for c in string:
        if c in data:
            data[c] += 1
        else:
            data[c] = 1

    data = sorted(data.items(), key=lambda x: x[1])
    print(data)
    size = len(data)
    makeHuffmanNone(data, size)
