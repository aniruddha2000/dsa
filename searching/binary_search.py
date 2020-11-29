def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return arr[mid]
        if x > arr[mid]:
            l = mid + 1
        if x < arr[mid]:
            r = mid - 1
    return False


arr = [10, 19, 25, 36, 55, 69, 78]
x = 55

a = binary_search(arr, 0, len(arr)-1, x)

if a == False:
    print("Element not found")
else:
    print("Element found " + str(a ))
