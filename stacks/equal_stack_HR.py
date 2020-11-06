def equalStacks(h1, h2, h3):
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    while not (sum_h1 == sum_h2 == sum_h3):
        if sum_h1 > sum_h2 or sum_h1 > sum_h3:
            sum_h1 -= h1.pop()
        if sum_h2 > sum_h1 or sum_h2 > sum_h3:
            sum_h2 -= h2.pop()
        if sum_h3 > sum_h1 or sum_h3 > sum_h2:
            sum_h3 -= h3.pop()
    return sum_h1


h1 = [1, 1, 1, 2, 3]
h2 = [2, 3, 4]
h3 = [1, 4, 1, 1]
equalStacks(h1, h2, h3)
