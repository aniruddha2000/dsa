from max_heap import build_heap, heapify

def heap_sort(arr):
    # Step 1: Build a max heap from the input
    build_heap(arr)

    # n = heap size
    heap_size = len(arr)
    # for i in range(n-1, 0, -1):
    #     arr[i], arr[0] = arr[0], arr[i]
    #     heapify(arr, i, 0)
    while heap_size > 1:
        arr[heap_size-1], arr[0], = arr[0], arr[heap_size-1]
        heap_size -= 1
        heapify(arr, heap_size, 0)


def print_heap(arr):
    n = len(arr)
    print("Sorted array representation of Heap is:")

    for i in range(n):
        print(arr[i], end = " ")
    print()

if __name__ == "__main__":
    arr = [ 1, 3, 5, 4, 6, 13,
            10, 9, 8, 15, 17 ]
    heap_sort(arr)
    print_heap(arr)
