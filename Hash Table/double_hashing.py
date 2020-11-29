def hash1(arr, t_size):
    return arr % t_size


def hash2(arr):
    return (7 - (arr % 7))


def double_hashing(arr, t_size, hash_table, n):
    for i in range(n):
        index1 = hash1(arr[i], t_size)
        # If collision occure
        if hash_table[index1] != -1:
            index2 = hash2(arr[i])
            j = 1
            while 1:
                new_indx = (index1 + (j * index2)) % t_size
                if hash_table[new_indx] == -1:
                    hash_table[new_indx] = arr[i]
                    break
                j += 1

        # No collision
        else:
            hash_table[index1] = arr[i]

    printArray(hash_table, t_size)


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


arr = [19, 27, 36, 10, 64]
# t_size = len(arr)
t_size = 13
n = len(arr)

hash_table = [0] * t_size
for i in range(t_size):
    hash_table[i] = -1

double_hashing(arr, t_size, hash_table, n)
