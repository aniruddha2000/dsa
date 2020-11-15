def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            v = arr[i]
            j = i
            while arr[j-gap] > v and j >= gap:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = v
        gap = gap // 2




arr = [64, 34, 25, 12, 22, 11, 90]

shellSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i], end=" ")
print()
