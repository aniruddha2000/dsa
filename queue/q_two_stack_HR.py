def main(n):
    s1 = []
    s2 = []
    for i in range(n):
        t = list(input().split())
        if int(t[0]) == 1:
            s1.append(int(t[1]))
        if int(t[0]) == 2:
            if len(s2) == 0 and len(s1) > 0:
                while len(s1) != 0:
                    s2.append(s1.pop())
                s2.pop()
            else:
                s2.pop()
        if int(t[0]) == 3:
            print(s2[-1] if s2 else s1[0])


if __name__ == "__main__":
    n = int(input())
    main(n)
