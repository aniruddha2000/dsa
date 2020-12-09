NO_OF_CHARS = 256

def badCharHeuristic(pat, m):
    badChar = [-1]*NO_OF_CHARS
    for i in range(m):
        badChar[ord(pat[i])] = i
    return badChar

def search(txt, pat):
    m = len(pat)
    n = len(txt)

    badChar = badCharHeuristic(pat, m)
    s = 0
    while s <= n-m:
        j = m -1
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
        if j<0:
            print("Pattern occur at shift = {}".format(s))
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])


txt = "ABAAABCD"
pat = "ABC"
search(txt, pat)
