import heapq


def cookies(k, a):
    c = 0
    heapq.heapify(a)
    while a[0] < k and len(a) >= 2:
        frst_cookie = heapq.heappop(a)
        scnd_cookie = heapq.heappop(a)
        new_cookie = (1 * frst_cookie) + (2 * scnd_cookie)
        heapq.heappush(a, new_cookie)
        c += 1
    if a[0] >= k:
        print(c)
    else:
        print("-1")



a = [1, 2, 3, 9, 10, 12]
cookies(7, a)
