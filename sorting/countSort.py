def count_sort(arr):
    max_ele = int(max(arr))

    count = [0 for i in range(max_ele+1)]

    for i in arr:
        count[i] += 1

    i, j = 0, 0
    while i < max_ele+1:
        if count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1
        i += 1


arr = [5, 6, 2, 9, 3, 7, 1]
count_sort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i], end=" ")
print()
