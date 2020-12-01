def search(pat, txt):
    n = len(txt)
    m = len(pat)
    for i in range(n - m):
        j = 0
        while j < m and pat[j] == txt[i+j]:
            j += 1
        if j == m:
            print("Pattern found at index " + str(i))



txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(pat, txt)
