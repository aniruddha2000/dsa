from collections import deque
from math import sqrt

def downToZero(n):
    memo = set()
    c = 0
    q = deque([[n, c]])
    while q:
        n, c = q.popleft()
        if n <= 1:
            if n == 1:
                c += 1
            break
        if n-1 not in memo:
            memo.add(n-1)
            q.append([n-1, c+1])
        for i in range(int(sqrt(n), 1, -1)):
            if n%i == 0:
                factor = max(n//i, i)
                if factor not in memo:
                    memo.add(factor)
                    q.append([factor, c+1])
    return c
