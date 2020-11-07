def twoStacks(x, a, b):
    i, j, sum = 0,0,0
    while i<len(a) and (sum+a[i])<=x:
        sum+=a[i]
        i+=1
    ans=i
    while j<len(b) and i>=0:
        sum+=b[j]
        j+=1
        while sum>x and i>0:
            i-=1
            sum-=a[i]
        if sum<=x and i+j>ans:
            ans=i+j
    return ans


a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]
x = 10
print(twoStacks(x, a, b))
