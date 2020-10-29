def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        a = arr[left]
        la = arr[largest]
        largest = left

    if right < n and arr[right] > arr[largest]:
        b = arr[right]
        la = arr[largest]
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr, n):
    startIndx = n // 2 - 1
    for i in range(startIndx, -1, -1):
        heapify(arr, n, i)

def printHeap(arr, n):
    print("Array representation of Heap is:");

    for i in range(n):
        print(arr[i], end = " ");
    print()


if __name__ == "__main__":
    arr = [ 1, 3, 5, 4, 6, 13,
            10, 9, 8, 15, 17 ]
    n = len(arr)
    build_heap(arr, n)
    printHeap(arr, n)
