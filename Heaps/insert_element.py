from Build_array import printHeap


def heapify(arr, n, i):
    if i != 0:
        parent = (i-1)//2
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            heapify(arr, n, parent)

def insert_ele(arr, n, data):
    n = n + 1
    arr.append(data)
    heapify(arr, n, n-1)
    return arr


arr = [10, 5, 3, 2, 4]
n = len(arr)
arr = insert_ele(arr, n, 15)
n = len(arr)
printHeap(arr, n)
