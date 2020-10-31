# MIN Heap

def heapify(arr, n, i):
    smallest = i
    leftChild = 2*i + 1
    rightChild = 2*i + 2

    if leftChild < n and arr[leftChild] < arr[smallest]:
        smallest = leftChild

    if rightChild < n and arr[rightChild] < arr[smallest]:
        smallest = rightChild

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def build_heap(arr, n):
    # Starting index that is last
    # non leaf node because leafs
    # already have heap property
    startIndx = n // 2 - 1
    for i in range(startIndx, -1, -1):
        heapify(arr, n, i)

def printHeap(arr, n):
    print("Array representation of Heap is:")

    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    arr = [1, 5, 6, 8, 9, 7, 3]
    n = len(arr)
    build_heap(arr, n)
    printHeap(arr, n)
