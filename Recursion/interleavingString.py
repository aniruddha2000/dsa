def findInterLeaving(str1, str2, result, m, n, i):
    if m==0 and n == 0:
        print(str(result))
    if m != 0:
        result[i] = str1[0]
        findInterLeaving(str1[1:], str2, result, m-1, n, i+1)
    if n != 0:
        result[i] = str2[0]
        findInterLeaving(str1, str2[1:], result, m, n-1, i+1)

str1 = "ABC"
str2 = "CDE"
m = len(str1)
n = len(str2)
result = ['']*(m+n)
findInterLeaving(str1, str2, result, m, n, 0)
