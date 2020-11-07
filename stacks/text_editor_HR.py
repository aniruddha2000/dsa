def main(n):
    stack = []
    s = ""
    for i in range(n):
        t = list(input().split())
        if int(t[0]) == 1:
            stack.append(s)
            s += str(t[1])
        if int(t[0]) == 2:
            stack.append(s)
            s = s[:-int(t[1])]
        if int(t[0]) == 3:
            print(s[int(t[1])-1])
        if int(t[0]) == 4:
            s = stack.pop()


if __name__ == "__main__":
    n = int(input())
    main(n)
