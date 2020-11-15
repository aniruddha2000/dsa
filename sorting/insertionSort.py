def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        v = arr[i]
        j = i
        while arr[j-1] > v and j >= 1:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v



arr = [64, 34, 25, 12, 22, 11, 90]

insertionSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i], end=" ")
print()
