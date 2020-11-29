def hashing(arr, t_size, hash_table, n):
    for i in range(n):
        hv = arr[i] % t_size
        if hash_table[hv] == -1:
            hash_table[hv] = arr[i]
        else:
            for j in range(t_size):
                t = (hv + j*j) % t_size
                if hash_table[t] == -1:
                    hash_table[t] = arr[i]
                    break
    printArray(hash_table, n)

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
    print()

arr = [50, 700, 76, 85, 92, 73, 101]
t_size = len(arr)
n = len(arr)

hash_table = [0] * t_size
for i in range(t_size):
    hash_table[i] = -1

hashing(arr, t_size, hash_table, n)
