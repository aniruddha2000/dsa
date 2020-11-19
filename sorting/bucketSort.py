def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        v = arr[i]
        j = i
        while arr[j-1] > v and j >= 1:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v
    return arr

def bucketSort(x):
    arr = []
    slot_num = 10

    # Create bucket
    for i in range(slot_num):
        arr.append([])

    # Insert in bucket
    for j in x:
        index = int(slot_num * j)
        arr[index].append(j)

    # Sort the bucket
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    # Concatenate the bucket
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))
