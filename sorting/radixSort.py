def countSort(arr, exp):
    size = len(arr)
    max_ele = int(max(arr))

    count = [0 for i in range(10)]
    output = [0 for i in range(size)]

    for i in range(0, size):
        index = (arr[i] / exp)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

def radixSort(arr):
    max_ele = max(arr)
    exp = 1
    while max_ele / exp > 0:
        countSort(arr, exp)
        exp *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
print()
