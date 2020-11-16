s = "PythON"
s = list(s)
i = k = 0
while i < len(s):
    if s[i].islower():
        s[i], s[k] = s[k], s[i]
        k += 1
    i += 1
s = ''.join(s)
print(s)
