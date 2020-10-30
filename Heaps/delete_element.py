from Build_array import heapify, printHeap

def delete_ele(arr, n):
    lst_ele = arr[-1]
    arr.pop()
    arr[0] = lst_ele
    n = n - 1
    heapify(arr, n, 0)
    return arr

arr = [10, 5, 3, 2, 4]
n = len(arr)
arr = delete_ele(arr, n)
n = len(arr)
printHeap(arr, n)
