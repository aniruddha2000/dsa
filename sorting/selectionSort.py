def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]




arr = [64, 34, 25, 12, 22, 11, 90]

selectionSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i], end=" ")
print()
