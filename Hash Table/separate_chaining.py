from collections import defaultdict

def separate_chaining(arr, hash_table, t_size, n):
    for i in range(n):
        index = arr[i] % t_size
        hash_table[index].append(arr[i])

    printArray(hash_table, t_size)


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


arr = [15, 11, 27, 8, 12]
t_size = 7
n = len(arr)

hash_table = defaultdict(list)
separate_chaining(arr, hash_table, t_size, n)
