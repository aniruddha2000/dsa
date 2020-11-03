import heapq


code = {}


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

def store_code(root, s):
    if root is None:
        return
    if root.data is not None:
        code[root.data] = s
    store_code(root.left, s+"0")
    store_code(root.right, s+"1")


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
    return root


def decode_string(root, s):
    curr = root
    ans = ""
    for i in range(0, len(s)):
        if s[i] == "0":
            curr = curr.left
        else:
            curr = curr.right

        if curr.left == None and curr.right == None:
            ans += curr.data
            curr = root
    return ans


if __name__ == "__main__":
    string = "BCAADDDCCACACAC"
    data = {}
    for c in string:
        if c in data:
            data[c] += 1
        else:
            data[c] = 1

    data = sorted(data.items(), key=lambda x: x[1])
    print("Frequency of data: ")
    print(data)
    size = len(data)
    root = makeHuffmanNone(data, size)
    print("\nEncoded Huffman data for each charater: ")
    printCode(root, "")
    store_code(root, "")
    encodedString = ""
    for i in string:
        encodedString+=code[i]
    print("\nEncoded Huffman String: ")
    print(encodedString)
    decodedString = decode_string(root, encodedString)
    print("\nDecoded string")
    print(decodedString)
